import warnings
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from typing import Optional

import yfinance as yf
from moneyed import Money

# ==============================================================================
# SECTION 1: HISTORICAL PRICE FETCHING FUNCTIONS
# ==============================================================================

def fetch_close_price(ticker: str, on_date: date) -> Optional[Decimal]:
    """
    Return the closing price as a Decimal for a specific ticker and date.
    For today's date, it fetches the most recent price available.
    """
    try:
        today = date.today()
        if on_date > today:
            return None
        
        tk = yf.Ticker(ticker)

        # For today's date, try fast_info then 1d history for the latest price
        if on_date == today:
            try:
                info = tk.fast_info
                last = info.get('last_price') or info.get('regularMarketPrice') or info.get('last_close')
                if last:
                    return Decimal(str(last))
            except Exception:
                pass # Fallback to history
            df = tk.history(period='1d')
            if not df.empty and 'Close' in df:
                return Decimal(str(df['Close'].iloc[-1]))
            return None

        # For past dates, fetch the exact closing price
        end_date = on_date + timedelta(days=1)
        df = tk.history(start=on_date, end=end_date, auto_adjust=True)
        if df.empty or 'Close' not in df:
            return None
        return Decimal(str(df['Close'].iloc[0]))
    except Exception as e:
        warnings.warn(f"Error fetching historical price for {ticker} on {on_date}: {e}", UserWarning)
        return None


def find_previous_close(ticker: str, on_date: date, max_days_ago: int = 30) -> Optional[Decimal]:
    """
    Searches backwards from a given date to find the first available closing price.
    """
    today = date.today()
    for days in range(0, max_days_ago):
        target_date = on_date - timedelta(days=days)
        if target_date > today:
            continue
        price = fetch_close_price(ticker, target_date)
        if price is not None:
            return price
    warnings.warn(f"No close price found in {max_days_ago} days before {on_date} for {ticker}.", UserWarning)
    return None


def find_next_open(ticker: str, on_date: date, max_days_forward: int = 30) -> Optional[Decimal]:
    """
    Searches forwards from a given date to find the next trading day's opening price.
    """
    today = date.today()
    tk = yf.Ticker(ticker)
    for days in range(1, max_days_forward + 1):
        target_date = on_date + timedelta(days=days)
        if target_date > today + timedelta(days=1): # Allow fetching for tomorrow
            break
        try:
            df = tk.history(start=target_date, end=target_date + timedelta(days=1))
            if not df.empty and 'Open' in df:
                return Decimal(str(df['Open'].iloc[0]))
        except Exception:
            continue # Try the next day
    warnings.warn(f"No next-day open found in {max_days_forward} days after {on_date} for {ticker}.", UserWarning)
    return None

# ==============================================================================
# SECTION 2: CURRENT PRICE VALUATION HELPER CLASS
# ==============================================================================

def guess_currency_from_ticker(ticker: str) -> str:
    """Guesses a stock's currency from its ticker suffix."""
    t = ticker.upper()
    if t.endswith(('.DE', '.MI', '.PA', '.MU', '.F')): return 'EUR'
    if t.endswith(('.L', '.LN')): return 'GBP'
    if t.endswith('.TO'): return 'CAD'
    if t.endswith('.SW'): return 'CHF'
    if t.endswith('.HK'): return 'HKD'
    if t.endswith(('.SS', '.SZ')): return 'CNY'
    return 'USD'


class StockValuationHelper:
    """
    A helper to fetch current stock prices with a manual input fallback.
    """
    def __init__(self, ticker: str):
        if not ticker:
            raise ValueError("Ticker must be provided.")
        self.ticker = ticker.upper()
        self.currency_code = guess_currency_from_ticker(self.ticker)
        self.tk = yf.Ticker(self.ticker)
        self.is_available = self._check_availability()

        if not self.is_available:
            warnings.warn(
                f"Ticker '{self.ticker}' seems unavailable or has no recent data. "
                "Functionality may be limited.",
                UserWarning
            )

    def _check_availability(self) -> bool:
        """Checks if the ticker has any market data."""
        try:
            # A short history check is the most robust way to check for a valid ticker
            if not self.tk.history(period='5d').empty:
                return True
            # As a fallback, check fast_info
            info = self.tk.fast_info
            if info.get('last_price') or info.get('currency'):
                return True
            return False
        except Exception:
            return False

    def get_current_price(self) -> Optional[Money]:
        """
        Tries to fetch the current market price automatically.
        If it fails, it prompts the user for manual input.
        """
        if self.is_available:
            price = fetch_close_price(self.ticker, date.today())
            if price is not None:
                return Money(price, self.currency_code)

        warnings.warn(
            f"Could not automatically fetch current price for {self.ticker}. "
            "Please provide it manually.",
            UserWarning
        )
        return self._prompt_for_manual_price()

    def _prompt_for_manual_price(self) -> Optional[Money]:
        """Prompts the user to enter the price and validates the input."""
        while True:
            try:
                user_input = input(
                    f"-> Enter the current price for one share of {self.ticker} "
                    f"in {self.currency_code}: "
                )
                if user_input.strip().lower() in ['q', 'quit', 'exit']:
                    warnings.warn("Manual price entry skipped by user.", UserWarning)
                    return None
                
                price_decimal = Decimal(user_input)
                
                if price_decimal < 0:
                    print("ERROR: Price cannot be negative. Please try again.")
                    continue
                    
                return Money(price_decimal, self.currency_code)

            except (InvalidOperation, ValueError):
                print("ERROR: Invalid input. Please enter a valid number (e.g., 150.75).")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return None