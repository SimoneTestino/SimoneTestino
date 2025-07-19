#!/usr/bin/env python3
"""
conversion_safe.py

Enhanced currency conversion with caching and automatic rate inversion.
"""

from decimal import Decimal, ROUND_HALF_UP
from moneyed import Money, get_currency, USD, EUR, GBP, CHF
from forex_python.converter import CurrencyRates, RatesNotAvailableError
import warnings
from typing import Dict, Tuple, Optional, Set

class CurrencyConverter:
    """
    Currency converter with caching and automatic fallback to manual rates.
    """
    def __init__(self):
        self.currency_rates = CurrencyRates()
        self.failed_pairs: Set[Tuple[str, str]] = set()
        self.live_rate_cache: Dict[Tuple[str, str], Decimal] = {}
        self.manual_rates: Dict[Tuple[str, str], Decimal] = {}

    def set_manual_rates(self, rates: Dict[Tuple[str, str], Decimal]) -> None:
        """
        Set manual exchange rates. Automatically calculates inverse rates.
        :param rates: Dict mapping (base, target) -> Decimal rate
        """
        self.manual_rates.clear()
        for (base, target), rate in rates.items():
            # Store the provided rate
            self.manual_rates[(base, target)] = rate
            # Calculate and store the inverse rate
            if rate != 0:
                inverse_rate = Decimal('1') / rate
                self.manual_rates[(target, base)] = inverse_rate

    def _get_live_rate(self, base: str, target: str) -> Optional[Decimal]:
        """
        Attempt to get live exchange rate with caching.
        :param base: Base currency code
        :param target: Target currency code  
        :return: Exchange rate as Decimal, or None if failed
        """
        pair = (base, target)
        # Check if this pair has already failed
        if pair in self.failed_pairs:
            return None
        # Check cache first
        if pair in self.live_rate_cache:
            return self.live_rate_cache[pair]
        # Attempt live lookup
        try:
            rate = Decimal(str(self.currency_rates.get_rate(base, target)))
            self.live_rate_cache[pair] = rate
            return rate
        except RatesNotAvailableError:
            # Mark this pair as failed to avoid future attempts
            self.failed_pairs.add(pair)
            return None
        except Exception:
            # Handle other potential errors (network issues, etc.)
            self.failed_pairs.add(pair)
            return None

    def _get_manual_rate(self, base: str, target: str) -> Optional[Decimal]:
        """
        Get manual exchange rate, checking both direct and inverse rates.
        :param base: Base currency code
        :param target: Target currency code
        :return: Exchange rate as Decimal, or None if not available
        """
        direct_key = (base, target)
        if direct_key in self.manual_rates:
            return self.manual_rates[direct_key]
        inverse_key = (target, base)
        if inverse_key in self.manual_rates:
            return self.manual_rates[inverse_key]
        return None

    def convert(self, money: Money, target: str) -> Money:
        """
        Convert a Money instance to target currency.
        1. Try live rate (unless previously failed)
        2. Fall back to manual rate with warning
        3. Raise ValueError if no rate available
        :param money: Source Money instance
        :param target: Target currency code (e.g., 'EUR')
        :return: Money in target currency
        :raises ValueError: If no exchange rate is available
        """
        base = money.currency.code
        # Same currency, no conversion needed
        if base == target:
            return money
        # Try live rate first
        live_rate = self._get_live_rate(base, target)
        if live_rate is not None:
            converted_amount = Decimal(str(money.amount)) * live_rate
            converted_amount = converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            return Money(converted_amount, get_currency(target))
        # Try manual rate
        manual_rate = self._get_manual_rate(base, target)
        if manual_rate is not None:
            warnings.warn(
                f"Live FX rate unavailable for {base}→{target}; using manual rate: {manual_rate}",
                UserWarning
            )
            converted_amount = Decimal(str(money.amount)) * manual_rate
            converted_amount = converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            return Money(converted_amount, get_currency(target))
        # No rate available
        raise ValueError(f"No FX rate available for {base}→{target}.")

    def clear_cache(self) -> None:
        """Clear all cached rates and failed pairs."""
        self.live_rate_cache.clear()
        self.failed_pairs.clear()

    def get_failed_pairs(self) -> Set[Tuple[str, str]]:
        """Get set of currency pairs that failed live lookup."""
        return self.failed_pairs.copy()

    def get_cached_rates(self) -> Dict[Tuple[str, str], Decimal]:
        """Get currently cached live rates."""
        return self.live_rate_cache.copy()

# Global converter instance for convenience
_converter = CurrencyConverter()

def conversion_safe(
    money: Money,
    target: str,
    manual_rates: Dict[Tuple[str, str], Decimal] = None
) -> Money:
    """
    Convenience function for currency conversion.
    :param money: Source Money instance
    :param target: Target currency code
    :param manual_rates: Optional manual rates (will be set globally)
    :return: Money in target currency
    """
    if manual_rates:
        _converter.set_manual_rates(manual_rates)
    return _converter.convert(money, target)

def set_manual_rates(rates: Dict[Tuple[str, str], Decimal]) -> None:
    """Set manual exchange rates globally."""
    _converter.set_manual_rates(rates)

def clear_conversion_cache() -> None:
    """Clear the global conversion cache."""
    _converter.clear_cache()

def get_conversion_stats() -> Dict[str, any]:
    """Get statistics about the global converter."""
    return {
        'failed_pairs': _converter.get_failed_pairs(),
        'cached_rates': _converter.get_cached_rates(),
        'manual_rates': _converter.manual_rates.copy()
    }

if __name__ == "__main__":
    # Example usage
    print("=== Currency Conversion Example ===")
    manual_rates = {
        ('EUR', 'USD'): Decimal('1.1658'),
        ('USD', 'EUR'): Decimal('0.8577'),
        ('EUR', 'CHF'): Decimal('0.9334'),
        ('CHF', 'EUR'): Decimal('1.0714'),
        ('USD', 'CHF'): Decimal('0.8035'),
        ('CHF', 'USD'): Decimal('1.2456'),
    }
    set_manual_rates(manual_rates)
    test_cases = [
        (Money(100, EUR), 'USD'),
        (Money(100, USD), 'EUR'),
        (Money(50, USD), 'GBP'),
        (Money(50, GBP), 'USD'),
        (Money(200, EUR), 'CHF'),
        (Money(100, EUR), 'CNY'),
        (Money(100, EUR), 'JPY'),
    ]
    for money, target in test_cases:
        try:
            result = conversion_safe(money, target)
            print(f"{money} → {result}")
        except ValueError as e:
            print(f"Failed: {money} → {target}: {e}")

    print("\n=== Conversion Statistics ===")
    stats = get_conversion_stats()
    print(f"Failed pairs: {stats['failed_pairs']}")
    print(f"Cached live rates: {len(stats['cached_rates'])}")
    print(f"Manual rates available: {len(stats['manual_rates'])}")

    print("\n=== Second Attempt (Should Use Cache) ===")
    result2 = conversion_safe(Money(100, EUR), 'USD')
    print(f"Second conversion: {result2}")

    print("\n=== Testing Failure Case ===")
    try:
        conversion_safe(Money(50, EUR), 'JPY')
    except ValueError as e:
        print(f"Expected failure: {e}")