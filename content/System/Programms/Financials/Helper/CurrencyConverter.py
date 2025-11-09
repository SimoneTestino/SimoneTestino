#!/usr/bin/env python3
"""
conversion_safe.py

Enhanced currency conversion using yfinance for live rates, with caching and manual fallbacks.
"""

import yfinance as yf
from decimal import Decimal, ROUND_HALF_UP
from moneyed import Money, get_currency, USD, EUR, GBP, CHF
import warnings
from typing import Dict, Tuple, Optional, Set

class CurrencyConverter:
    """
    Currency converter using yfinance for live rates, with caching, fallback to manual rates,
    and a manual-only switch.
    """
    def __init__(self, force_manual: bool = False):
        """
        Initializes the converter.
        :param force_manual: If True, disables live API calls and uses only manual rates.
        """
        self.failed_pairs: Set[Tuple[str, str]] = set()
        self.live_rate_cache: Dict[Tuple[str, str], Decimal] = {}
        self.manual_rates: Dict[Tuple[str, str], Decimal] = {}
        self.force_manual = force_manual

    def set_force_manual(self, force: bool) -> None:
        """
        Set the converter to force manual-only lookups, skipping live API calls.
        :param force: True to disable live API calls, False to re-enable them.
        """
        self.force_manual = force

    def set_manual_rates(self, rates: Dict[Tuple[str, str], Decimal]) -> None:
        """
        Set manual exchange rates. Automatically calculates inverse rates.
        :param rates: Dict mapping (base, target) -> Decimal rate
        """
        self.manual_rates.clear()
        for (base, target), rate in rates.items():
            self.manual_rates[(base.upper(), target.upper())] = rate
            if rate != 0:
                inverse_rate = Decimal('1') / rate
                self.manual_rates[(target.upper(), base.upper())] = inverse_rate

    def _get_live_rate(self, base: str, target: str) -> Optional[Decimal]:
        """
        --- FIXED: Fetches live exchange rate using the more reliable yfinance.history() ---
        """
        pair = (base, target)
        if pair in self.failed_pairs:
            return None
        if pair in self.live_rate_cache:
            return self.live_rate_cache[pair]
        
        try:
            ticker_str = f"{base}{target}=X"
            ticker = yf.Ticker(ticker_str)
            
            # Use the more robust history() method to get the last closing price
            hist = ticker.history(period="1d")
            
            if not hist.empty:
                price = hist['Close'].iloc[-1]
                rate = Decimal(str(price))
                self.live_rate_cache[pair] = rate
                return rate
            else:
                # If history is empty, treat as a failure
                self.failed_pairs.add(pair)
                return None
        except Exception:
            # Catch any exception from yfinance (e.g., invalid ticker, network error)
            self.failed_pairs.add(pair)
            return None

    def _get_manual_rate(self, base: str, target: str) -> Optional[Decimal]:
        """Get manual exchange rate."""
        return self.manual_rates.get((base, target))

    def convert(self, money: Money, target: str) -> Money:
        """
        Convert a Money instance to target currency.
        Respects the 'force_manual' switch to skip live lookups.
        """
        base = money.currency.code
        target = target.upper()
        if base == target:
            return money

        rate = None
        
        # 1. Try live rate only if manual mode is NOT forced.
        if not self.force_manual:
            rate = self._get_live_rate(base, target)
        
        # 2. If live rate was skipped or failed, try manual rate.
        if rate is None:
            manual_rate = self._get_manual_rate(base, target)
            if manual_rate is not None:
                rate = manual_rate
                if not self.force_manual:
                    warnings.warn(f"Live FX rate for {base}→{target} failed; using manual rate: {rate}", UserWarning)
            else:
                # 3. No rate could be found.
                if self.force_manual:
                    raise ValueError(f"No MANUAL rate for {base}→{target} (manual mode forced).")
                else:
                    raise ValueError(f"No rate available for {base}→{target} (live & manual failed).")

        converted_amount = (Decimal(str(money.amount)) * rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return Money(converted_amount, get_currency(target))

    def clear_cache(self) -> None:
        self.live_rate_cache.clear()
        self.failed_pairs.clear()

# Global instance and helper functions
_converter = CurrencyConverter()

def set_force_manual_mode(force: bool) -> None:
    _converter.set_force_manual(force)

def conversion_safe(
    money: Money,
    target: str,
    manual_rates: Optional[Dict[Tuple[str, str], Decimal]] = None,
) -> Money:
    if manual_rates:
        _converter.set_manual_rates(manual_rates)
    return _converter.convert(money, target)

def set_manual_rates(rates: Dict[Tuple[str, str], Decimal]) -> None:
    _converter.set_manual_rates(rates)

# Main example
if __name__ == "__main__":
    manual_rates = {
        ('EUR', 'USD'): Decimal('1.08'),
        ('EUR', 'CHF'): Decimal('0.98'),
    }
    set_manual_rates(manual_rates)
    print("=== Default Mode (Live with Manual Fallback) ===")
    try:
        # This should now work using the live rate from yfinance.history()
        gbp_to_eur = conversion_safe(Money(100, GBP), 'EUR')
        print(f"✅ {Money(100, GBP)} → {gbp_to_eur} (Live from yfinance)")
    except ValueError as e:
        print(f"❌ Live conversion failed: {e}")
    
    try:
        # This should also try the live rate first, and succeed.
        eur_to_usd = conversion_safe(Money(100, EUR), 'USD')
        print(f"✅ {Money(100, EUR)} → {eur_to_usd} (Live from yfinance)")
    except ValueError as e:
        print(f"❌ Live conversion failed: {e}")

    print("\n" + "="*50 + "\n")

    print("=== Manual-Only Mode (force_manual = True) ===")
    set_force_manual_mode(True)

    try:
        # This conversion will still FAIL because there's no manual rate for GBP->EUR
        gbp_to_eur_manual = conversion_safe(Money(100, GBP), 'EUR')
        print(f"✅ {Money(100, GBP)} → {gbp_to_eur_manual}")
    except ValueError as e:
        print(f"❌ {Money(100, GBP)} → EUR: {e}")
    
    try:
        # This conversion still WORKS because the manual rate exists
        eur_to_usd_manual = conversion_safe(Money(100, EUR), 'USD')
        print(f"✅ {Money(100, EUR)} → {eur_to_usd_manual} (Manual rate found)")
    except ValueError as e:
        print(f"❌ Manual conversion failed: {e}")
    
    # Set back to default mode
    set_force_manual_mode(False)