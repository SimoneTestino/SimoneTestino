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
    sys.path.insert(0, parent_dir)  # insert at beginning to prioritise

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
    Manages an exchange-traded asset with robust handling and today's price support.
    This version is refactored to use external helpers for price fetching and currency conversion.
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
        Initializes the LiquidAsset, relying on helper functions for market data.
        """
        if not ticker:
            raise ValueError("Ticker must be provided")
        self.ticker = ticker.upper()
        self.exchange = exchange

        self.name = name
        self.asset_class = 'market'
        self.quantity = quantity

        if instrument_type not in INSTRUMENT_TYPES:
            warnings.warn(f"Unknown instrument_type '{instrument_type}'; defaulting to 'other'.")
            instrument_type = 'other'
        self.instrument_type = instrument_type

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

        if geography not in GEOGRAPHIES:
            warnings.warn(f"Unknown geography '{geography}'; defaulting to 'Global'.")
            geography = 'Global'
        self.geography = geography
        self.isin = isin

        self._valuation_helper = StockValuationHelper(self.ticker)
        self.is_available = self._valuation_helper.is_available

        currency_code = self._valuation_helper.currency_code
        if purchase_price is None and purchase_date and self.is_available:
            prev = find_previous_close(self.ticker, purchase_date)
            if prev is not None:
                purchase_price = Money(prev, get_currency(currency_code))
            else:
                warnings.warn(f"Could not fetch purchase price for {self.ticker} on {purchase_date}")
                purchase_price = Money(0, get_currency(currency_code))
        elif purchase_price is None:
            purchase_price = Money(0, get_currency(currency_code))

        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.leverage = leverage if leverage > 0 else 1.0

        qty = Decimal(str(self.quantity))
        lev = Decimal(str(self.leverage))
        base = Decimal(str(self.purchase_price.amount))
        invested = base * qty * lev
        self.initial_value = Money(invested, self.purchase_price.currency)
        self.current_value = self.initial_value

        self._converter = CurrencyConverter()

        self.price_checks: List[Tuple[date, Money, Money, Decimal, float]] = []
        if price_checks_input:
            if self.is_available:
                self._process_price_checks(price_checks_input)
            else:
                warnings.warn("Price checks skipped for unavailable ticker.")

    def _process_price_checks(self, price_checks: List[Tuple[date, Money]]):
        """
        Process historical price checks using helper functions.
        """
        for chk_date, provided in price_checks:
            if chk_date > date.today():
                warnings.warn(f"Skipping future date {chk_date}.")
                continue

            fetched = find_previous_close(self.ticker, chk_date)
            if fetched is None:
                warnings.warn(f"No close data for price check on {chk_date}.")
                continue

            hist_money = Money(fetched, provided.currency)
            dev_pct = float(abs(fetched - Decimal(str(provided.amount))) / Decimal(str(provided.amount)) * 100) if provided.amount > 0 else 0.0
            nxt = find_next_open(self.ticker, chk_date)
            interval = abs(nxt - fetched) if nxt is not None else Decimal('0')

            if dev_pct > 5.0:
                warnings.warn(f"Deviation {dev_pct:.2f}% on {chk_date} >5% threshold.")
            self.price_checks.append((chk_date, provided, hist_money, interval, dev_pct))

    def fetch_current_price(self) -> Optional[Money]:
        """
        Fetch latest market price using the StockValuationHelper.
        """
        return self._valuation_helper.get_current_price()

    def update_market_value(self) -> None:
        """Refresh current valuation by fetching the latest price."""
        price = self.fetch_current_price()
        if price:
            amt = Decimal(str(price.amount)) * Decimal(str(self.quantity)) * Decimal(str(self.leverage))
            self.current_value = Money(amt, price.currency)
        else:
            warnings.warn(f"Using initial value for {self.ticker} due to fetch failure.")

    def compute_profit(self) -> Money:
        """Compute absolute P/L."""
        diff = self.current_value.amount - self.initial_value.amount
        return Money(diff, self.initial_value.currency)

    def compute_return(self) -> float:
        """Compute P/L percentage."""
        init = self.initial_value.amount
        return 0.0 if init == 0 else float((self.current_value.amount - init) / init)

    def convert_to(self, target_currency: str) -> Money:
        """
        Convert current value to another currency using the safe converter helper.
        """
        try:
            return self._converter.convert(self.current_value, target_currency.upper())
        except ValueError as e:
            warnings.warn(f"Conversion failed for {self.ticker}: {e}")
            return self.current_value

    def to_eur(self) -> Money:
        """Convenience method to convert the current value to EUR."""
        return self.convert_to('EUR')

    def summary(self) -> str:
        """Generate a string summary of the asset."""
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
            f"- Initial value: {self.initial_value}",
            f"- Current value: {self.current_value}",
            f"- Profit: {self.compute_profit()}",
            f"- Return: {self.compute_return():.2%}"
        ]
        if self.price_checks:
            lines.append("- Price checks:")
            for d, p, h, i, dev in self.price_checks:
                lines.append(f"  * {d}: provided {p}, fetched {h}, dev {dev:.2f}%")
        return "\n".join(lines)
