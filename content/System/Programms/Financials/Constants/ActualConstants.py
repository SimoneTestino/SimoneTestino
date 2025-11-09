#!/usr/bin/env python3
"""
ActualConstants.py
Complete portfolio configuration with all assets. This file defines the assets
and populates the portfolio object.
"""

import sys
import os
from datetime import date, timedelta
from decimal import Decimal

# --- Path Setup ---
# Assumes this file is in a 'Constants' directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from moneyed import Money
from FinancialClasses.Liquidity import Liquidity
from FinancialClasses.Credit import Credit
from FinancialClasses.Debit import Debit
from FinancialClasses.LiquidAssets import LiquidAssets
from FinancialClasses.IlliquidAsset import IlliquidAsset
from FinancialClasses.Salary import Salary
from FinancialClasses.Portfolio import Portfolio
from Helper.CurrencyConverter import set_manual_rates

# --- Date and Exchange Rates ---
valuation_date = date(2025, 7, 26)
manual_rates = {
    ('EUR', 'USD'): Decimal('1.0825'),
    ('USD', 'EUR'): Decimal('0.9238'),
    ('EUR', 'CHF'): Decimal('0.9815'),
    ('CHF', 'EUR'): Decimal('1.0188'),
}
set_manual_rates(manual_rates)

# --- Liquidity Assets ---
cash_chf = Liquidity(name="Cash (CHF)", amount=Money(30, "CHF"), storage="Wallet")
cash_eur = Liquidity(name="Cash (EUR)", amount=Money(150, "EUR"), storage="Wallet")
bank_eur = Liquidity(name="ISP Bank Account", amount=Money(5950, "EUR"), storage="Bank Account")

# --- Illiquid Assets ---
macbook = IlliquidAsset(
    name="MacBook Pro 14\" M4", purchase_price=Money(2200, "EUR"),
    purchase_date=date(2025, 7, 1), valuations=[(valuation_date, Money(1200, "EUR"))],
    long_term_growth_rate=-0.10, end_of_life_date=valuation_date.replace(year=valuation_date.year + 7)
)
ipad = IlliquidAsset(
    name="iPad Air", purchase_price=Money(500, "EUR"),
    purchase_date=date(2023, 9, 10), valuations=[(valuation_date, Money(250, "EUR"))],
    long_term_growth_rate=-0.10, end_of_life_date=valuation_date.replace(year=valuation_date.year + 3)
)

# --- Credits and Debts ---
repayment_date = valuation_date + timedelta(days=7)
debit_fine = Debit(
    creditor="Lieven De Key", principal=Money(70, "EUR"),
    debit_type="planned", repayment_schedule=[(repayment_date, Money(70, "EUR"))]
)
reka = Credit(debtor="SBB", principal=Money(80, "CHF"), credit_type="conditional")
futura_july_receivable = Credit(
    debtor="Futura", principal=Money(450, "EUR"), credit_type="planned",
    repayment_schedule=[(date(2025, 7, 31), Money(450, "EUR"))]
)
futura_august_special = Credit(
    debtor="Futura", principal=Money(1100, "EUR"), credit_type="planned",
    repayment_schedule=[(date(2025, 8, 31), Money(1100, "EUR"))]
)
ryanair_claim = Credit(
    debtor="Ryanair", principal=Money(950, "EUR"), credit_type="planned",
    repayment_schedule=[(date(2025, 7, 31), Money(950, "EUR"))]
)

# --- Future Income Streams ---
futura_salary = Salary(
    employer="Futura (Tutoring)", payment=Money(390, "EUR"),
    frequency='monthly', start_date=date(2025, 7, 1)
)

# --- Market Assets (Stocks & ETFs) with Geographical Data ---
china_etf = LiquidAssets(
    name="iShares MSCI China A UCITS ETF USD (Acc)", ticker="36BZ.DE", quantity=1000,
    purchase_date=date(2025, 7, 1), instrument_type="ETF", etf_subtype="stocks",
    isin="IE00BQT3WG13", geography="China"
)
cl2_etf = LiquidAssets(
    name="MSCI USA 2x Leveraged ETF", ticker="CL2.DE", quantity=360,
    purchase_date=date(2025, 7, 1), instrument_type="ETF", etf_subtype="stocks",
    leverage=2.0, isin="FR0010755611", geography="USA"
)
baba = LiquidAssets(
    name="Alibaba", ticker="BABA", quantity=50, purchase_date=date(2025, 7, 1),
    instrument_type="stock", geography="China"
)
bidu = LiquidAssets(
    name="Baidu", ticker="BIDU", quantity=45, purchase_date=date(2025, 7, 1),
    instrument_type="stock", geography="China"
)
icga = LiquidAssets(
    name="iShsIV-MSCI China ETF", ticker="ICGA.DE", quantity=710,
    purchase_date=date(2025, 7, 1), instrument_type="ETF", etf_subtype="stocks",
    isin="IE00BJ5JPG56", geography="China"
)
zprv = LiquidAssets(
    name="SPDR S&P 400 US Mid Cap Value ETF", ticker="ZPRV.DE", quantity=51,
    purchase_date=date(2025, 7, 1), instrument_type="stock", isin="IE00BSPLC413",
    geography="USA"
)
nke = LiquidAssets(
    name="Nike", ticker="NKE", quantity=30, purchase_date=date(2025, 7, 1),
    instrument_type="stock", geography="USA"
)

# --- Portfolio Initialization ---
portfolio = Portfolio(valuation_date=valuation_date)
all_assets = [
    cash_chf, cash_eur, bank_eur,
    macbook, ipad,
    debit_fine,
    reka, futura_july_receivable, futura_august_special, ryanair_claim,
    futura_salary,
    china_etf, cl2_etf, baba, bidu, icga, zprv, nke
]
for asset in all_assets:
    portfolio.add_asset(asset)

print("ActualConstants initialized successfully.")