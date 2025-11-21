import sys
import os
import warnings
from datetime import date, timedelta
from typing import Optional, Literal, List, Tuple
from decimal import Decimal
from moneyed import Money, get_currency

# --- Add the parent directory to sys.path ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# --- Local Helper Imports ---
from Helper.FetchStockPrice import (
    fetch_close_price,
    find_previous_close,
    find_next_open,
    guess_currency_from_ticker,
    StockValuationHelper,
)
from Helper.CurrencyConverter import CurrencyConverter

# --- Constants ---
INSTRUMENT_TYPES = ['stock', 'ETF', 'bond', 'other']
ETF_SUBTYPES     = ['stocks', 'bonds', 'mixed']
GEOGRAPHIES      = ['USA', 'Europe', 'Emerging markets', 'China', 'Global', 'Else']

InstrumentType = Literal['stock', 'ETF', 'bond', 'other']
ETFSubtype     = Literal['stocks', 'bonds', 'mixed']
Geography      = Literal['USA', 'Europe', 'Emerging markets', 'China', 'Global', 'Else']

class LiquidAssets:
    """
    Manages an exchange-traded asset with proper leverage handling.
    Separates actual money invested from leveraged portfolio exposure.
    """

    def __init__(
        self,
        name: str,
        ticker: str,
        quantity: float,
        purchase_price: Optional[Money] = None,
        purchase_date: Optional[date]  = None,
        isin: Optional[str]            = None,
        exchange: Optional[str]        = None,
        instrument_type: InstrumentType = 'ETF',
        etf_subtype: Optional[ETFSubtype] = None,
        leverage: float                = 1.0,
        geography: Geography           = 'Global',
        price_checks_input: Optional[List[Tuple[date, Money]]] = None
    ):
        """
        Initializes the LiquidAsset with proper leverage separation.
        """
        if not ticker:
            raise ValueError("Ticker must be provided")

        self.ticker = ticker.upper()
        self.exchange = exchange
        self.name = name
        self.asset_class = 'market'
        self.quantity = quantity

        # Validate instrument type
        if instrument_type not in INSTRUMENT_TYPES:
            warnings.warn(f"Unknown instrument_type '{instrument_type}'; defaulting to 'other'.")
            instrument_type = 'other'
        self.instrument_type = instrument_type

        # Handle ETF specifics
        self.etf_subtype = None
        if instrument_type == 'ETF':
            if etf_subtype in ETF_SUBTYPES:
                self.etf_subtype = etf_subtype
            else:
                warnings.warn("Invalid or missing ETF subtype; defaulting to 'mixed'.")
                self.etf_subtype = 'mixed'
            if not isin:
                warnings.warn(f"Missing ISIN for ETF '{name}'.")
        elif etf_subtype is not None:
            warnings.warn("etf_subtype provided but instrument_type != 'ETF'; ignoring.")

        # Validate geography
        if geography not in GEOGRAPHIES:
            warnings.warn(f"Unknown geography '{geography}'; defaulting to 'Global'.")
            geography = 'Global'
        self.geography = geography
        self.isin = isin

        # Initialize StockValuationHelper
        self._valuation_helper = StockValuationHelper(self.ticker)
        self.is_available = self._valuation_helper.is_available
        currency_code = self._valuation_helper.currency_code

        # Handle purchase price logic with manual fallback
        if purchase_price is None and purchase_date:
            purchase_price = self._determine_purchase_price(purchase_date, currency_code)
        elif purchase_price is None:
            purchase_price = Money(0, get_currency(currency_code))

        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.leverage = leverage if leverage > 0 else 1.0

        # CRITICAL FIX: Separate actual investment from leveraged exposure
        qty = Decimal(str(self.quantity))
        lev = Decimal(str(self.leverage))
        base = Decimal(str(self.purchase_price.amount))
        
        # Actual money invested (NO leverage)
        actual_invested = base * qty
        self.actual_invested = Money(actual_invested, self.purchase_price.currency)
        
        # Portfolio exposure (WITH leverage for weighting)
        leveraged_invested = base * qty * lev
        self.initial_value = Money(leveraged_invested, self.purchase_price.currency)
        
        # Current value starts as initial (will be updated)
        self.current_value = self.initial_value
        self.actual_current_value = self.actual_invested  # Unleveraged current value

        # Initialize currency converter
        self._converter = CurrencyConverter()

        # Process price checks
        self.price_checks: List[Tuple[date, Money, Money, Decimal, float]] = []
        if price_checks_input:
            self._process_price_checks(price_checks_input)

    def _determine_purchase_price(self, purchase_date: date, currency_code: str) -> Money:
        """Determine purchase price with automatic fetch and manual fallback."""
        # Try automatic historical fetch first
        fetched_price = find_previous_close(self.ticker, purchase_date)
        
        if fetched_price is not None:
            return Money(fetched_price, get_currency(currency_code))
        
        # If automatic fetch fails, warn and attempt manual input
        warnings.warn(f"Could not fetch purchase price for {self.ticker} on {purchase_date}")
        
        print(f"\nAutomatic price fetch failed for {self.ticker} on {purchase_date}")
        print("Would you like to enter the purchase price manually?")
        
        try:
            manual_price = self._valuation_helper._prompt_for_manual_price()
            if manual_price:
                return manual_price
        except (KeyboardInterrupt, EOFError):
            warnings.warn("Manual price entry cancelled by user.")
        except Exception as e:
            warnings.warn(f"Error during manual price entry: {e}")
        
        # Fallback to zero
        warnings.warn(f"Using zero purchase price for {self.ticker}")
        return Money(0, get_currency(currency_code))

    def _process_price_checks(self, price_checks: List[Tuple[date, Money]]):
        """Process historical price checks using helper functions."""
        for chk_date, provided in price_checks:
            if chk_date > date.today():
                warnings.warn(f"Skipping future date {chk_date}.")
                continue

            # Use helper function to get historical price
            fetched = find_previous_close(self.ticker, chk_date)
            if fetched is None:
                warnings.warn(f"No close data for price check on {chk_date}.")
                continue

            hist_money = Money(fetched, provided.currency)
            
            # Calculate deviation percentage
            if provided.amount > 0:
                dev_pct = float(abs(fetched - Decimal(str(provided.amount))) / Decimal(str(provided.amount)) * 100)
            else:
                dev_pct = 0.0

            # Get next trading day's open for interval calculation
            nxt = find_next_open(self.ticker, chk_date)
            interval = abs(nxt - fetched) if nxt is not None else Decimal('0')

            # Warn if significant deviation
            if dev_pct > 5.0:
                warnings.warn(f"Price check deviation {dev_pct:.2f}% on {chk_date} exceeds 5% threshold.")

            self.price_checks.append((chk_date, provided, hist_money, interval, dev_pct))

    def fetch_current_price(self) -> Optional[Money]:
        """Fetch latest market price using StockValuationHelper with manual fallback."""
        try:
            current_price = self._valuation_helper.get_current_price()
            return current_price
        except Exception as e:
            warnings.warn(f"Error fetching current price for {self.ticker}: {e}")
            return None

    def update_market_value(self) -> None:
        """
        CRITICAL FIX: Update both leveraged and actual current values.
        """
        price = self.fetch_current_price()
        
        if price:
            qty = Decimal(str(self.quantity))
            lev = Decimal(str(self.leverage))
            price_amt = Decimal(str(price.amount))
            
            # Actual current value (NO leverage) - actual money you could get
            actual_current = price_amt * qty
            self.actual_current_value = Money(actual_current, price.currency)
            
            # Leveraged current value (WITH leverage) - for portfolio weighting
            leveraged_current = price_amt * qty * lev
            self.current_value = Money(leveraged_current, price.currency)
        else:
            warnings.warn(f"Could not update market value for {self.ticker}; using initial values.")

    def compute_profit(self) -> Money:
        """Compute leveraged profit/loss for portfolio calculations."""
        diff = self.current_value.amount - self.initial_value.amount
        return Money(diff, self.initial_value.currency)
    
    def compute_actual_profit(self) -> Money:
        """Compute actual profit/loss (without leverage multiplier)."""
        diff = self.actual_current_value.amount - self.actual_invested.amount
        return Money(diff, self.actual_invested.currency)

    def compute_return(self) -> float:
        """Compute percentage return based on actual investment."""
        actual = self.actual_invested.amount
        return 0.0 if actual == 0 else float(self.compute_actual_profit().amount / actual)

    def convert_to(self, target_currency: str) -> Money:
        """Convert leveraged current value to another currency."""
        try:
            return self._converter.convert(self.current_value, target_currency.upper())
        except ValueError as e:
            warnings.warn(f"Currency conversion failed for {self.ticker}: {e}")
            return self.current_value

    def convert_actual_to(self, target_currency: str) -> Money:
        """Convert actual current value to another currency."""
        try:
            return self._converter.convert(self.actual_current_value, target_currency.upper())
        except ValueError as e:
            warnings.warn(f"Currency conversion failed for {self.ticker}: {e}")
            return self.actual_current_value

    def to_eur(self) -> Money:
        """Convert leveraged value to EUR."""
        return self.convert_to('EUR')
    
    def actual_to_eur(self) -> Money:
        """Convert actual value to EUR."""
        return self.convert_actual_to('EUR')

    def get_historical_price(self, target_date: date) -> Optional[Money]:
        """Get historical price for a specific date using helper functions."""
        price_decimal = find_previous_close(self.ticker, target_date)
        if price_decimal is None:
            return None
        return Money(price_decimal, self._valuation_helper.currency_code)

    def force_manual_price_update(self) -> bool:
        """Force a manual price entry for current valuation."""
        try:
            print(f"\nForce manual price update for {self.ticker}")
            manual_price = self._valuation_helper._prompt_for_manual_price()
            if manual_price:
                qty = Decimal(str(self.quantity))
                lev = Decimal(str(self.leverage))
                price_amt = Decimal(str(manual_price.amount))
                
                # Update both values
                self.actual_current_value = Money(price_amt * qty, manual_price.currency)
                self.current_value = Money(price_amt * qty * lev, manual_price.currency)
                return True
        except (KeyboardInterrupt, EOFError):
            print("\nManual price update cancelled.")
        except Exception as e:
            warnings.warn(f"Error during manual price update: {e}")
        return False

    def summary(self) -> str:
        """Generate a comprehensive summary showing both actual and leveraged values."""
        avail = "✓ Available" if self.is_available else "⚠ Unavailable"
        lines = [
            f"{self.name} ({self.ticker}) - {avail}",
            f"- ISIN: {self.isin or 'N/A'}",
            f"- Type: {self.instrument_type}"
        ]

        if self.instrument_type == 'ETF':
            lines.append(f"- ETF subtype: {self.etf_subtype}")

        lines += [
            f"- Geography: {self.geography}",
            f"- Leverage: {self.leverage}x",
            f"- Purchased: {self.purchase_date} at {self.purchase_price} × {self.quantity}",
            "",
            f"ACTUAL INVESTMENT (No Leverage):",
            f"- Money invested: {self.actual_invested}",
            f"- Current value: {self.actual_current_value}",
            f"- Actual profit: {self.compute_actual_profit()}",
            f"- Return: {self.compute_return():.2%}",
            "",
            f"PORTFOLIO EXPOSURE (With {self.leverage}x Leverage):",
            f"- Initial exposure: {self.initial_value}",
            f"- Current exposure: {self.current_value}",
            f"- Leveraged profit: {self.compute_profit()}"
        ]

        if self.price_checks:
            lines.append("\n- Price checks:")
            for d, p, h, i, dev in self.price_checks:
                lines.append(f"  * {d}: provided {p}, fetched {h}, dev {dev:.2f}%")

        return "\n".join(lines)