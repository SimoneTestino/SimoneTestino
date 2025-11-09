#!/usr/bin/env python3
"""
HyperDebitScenarioAug25.py

This script defines a future financial plan with a simple, unleveraged investment strategy.
"""

import sys
import os
from datetime import date
from decimal import Decimal
from moneyed import Money
from dateutil.relativedelta import relativedelta

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Imports ---
from FinancialClasses.Portfolio import Portfolio
from FinancialClasses.PortfolioInTime import PortfolioInTime
from FinancialClasses.LiquidAssets import LiquidAssets
from FinancialClasses.IlliquidAsset import IlliquidAsset
from FinancialClasses.Liquidity import Liquidity
from FinancialClasses.Credit import Credit
from FinancialClasses.Debit import Debit
from Constants.ActualConstants import portfolio as initial_portfolio

# --- Helper function for generating loan schedules ---
def generate_repayment_schedule(principal: Money, rate: float, term_years: int, start_date: date) -> list:
    schedule = []
    r = Decimal(str(rate)) / 12
    n = term_years * 12
    principal_amount = abs(principal.amount)
    if r == 0:
        monthly_payment = principal_amount / n
    else:
        monthly_payment = principal_amount * (r * (1 + r)**n) / ((1 + r)**n - 1)
    for i in range(n):
        payment_date = start_date + relativedelta(months=+i)
        schedule.append((payment_date, Money(-monthly_payment, principal.currency)))
    return schedule

# --- 1. Define the Timeline and Future Assets ---
timeline = PortfolioInTime(initial_portfolio)
print("Initialized timeline with current portfolio.")

# --- Define all new assets and liabilities for the scenario ---
new_house = IlliquidAsset(
    name="House in Savona", purchase_price=Money(216666, "EUR"),
    purchase_date=date(2025, 9, 15),
    valuations=[(date(2025, 9, 15), Money(216666, "EUR"))]
)
student_loan = Debit(
    creditor="ISP - Prestito per Merito", principal=Money(-75000, "EUR"),
    debit_type="planned", interest_rate=0.025,
    repayment_schedule=generate_repayment_schedule(Money(-75000, "EUR"), 0.025, 30, date(2028, 9, 1)),
    origination_date=date(2025, 9, 1)
)
business_loan = Debit(
    creditor="ISP - Credito d'Impresa", principal=Money(-(216666 - 130000), "EUR"),
    debit_type="planned", interest_rate=0.03,
    repayment_schedule=generate_repayment_schedule(Money(-86666, "EUR"), 0.03, 10, date(2025, 9, 15)),
    origination_date=date(2025, 9, 15)
)

# Define the ETF investments (now unleveraged)
first_investment_cash = (30000 + 37500) # Cash from sold assets + first loan tranche
world_etf_1 = LiquidAssets(
    name="Vanguard FTSE All-World ETF", ticker="VWCE.DE", quantity=1,
    purchase_price=Money(first_investment_cash, "EUR"), instrument_type="ETF",
    etf_subtype="stocks", geography="Global", isin="IE00BK5BQT80", leverage=1.0
)

second_investment_cash = 37500
world_etf_2 = LiquidAssets(
    name="Vanguard FTSE All-World ETF (Consolidated)", ticker="VWCE.DE", quantity=1,
    purchase_price=Money(first_investment_cash + second_investment_cash, "EUR"),
    instrument_type="ETF", etf_subtype="stocks", geography="Global", isin="IE00BK5BQT80", leverage=1.0
)

# --- 2. Schedule the Modifications on the Timeline ---
print("\n" + "="*50)
print("      Scheduling Future Modifications (Simple Investment)")
print("="*50)

# --- September 1, 2025 ---
sept_1_2025 = date(2025, 9, 1)
for asset in initial_portfolio.assets:
    if isinstance(asset, LiquidAssets):
        timeline.add_modification(sept_1_2025, 'remove', asset)
        print(f"-> {sept_1_2025}: Scheduled SELL of {asset.name}")

timeline.add_modification(sept_1_2025, 'add', student_loan)
timeline.add_modification(sept_1_2025, 'add', Liquidity(name="ISP Loan Tranche 1", amount=Money(37500, "EUR"), storage="Bank"))
timeline.add_modification(sept_1_2025, 'add', world_etf_1)
print(f"-> {sept_1_2025}: ADD Student Loan and BUY World ETF for €{first_investment_cash:,.2f}.")

# --- September 15, 2025 ---
sept_15_2025 = date(2025, 9, 15)
timeline.add_modification(sept_15_2025, 'add', Liquidity(name="EU Funds Savonese", amount=Money(130000, "EUR"), storage="Bank"))
timeline.add_modification(sept_15_2025, 'add', business_loan)
timeline.add_modification(sept_15_2025, 'add', new_house)
print(f"-> {sept_15_2025}: ADD EU Funds, Business Loan, and PURCHASE House.")

# --- March 1, 2026 ---
march_1_2026 = date(2026, 3, 1)
timeline.add_modification(march_1_2026, 'add', Liquidity(name="ISP Loan Tranche 2", amount=Money(37500, "EUR"), storage="Bank"))
timeline.add_modification(march_1_2026, 'remove', world_etf_1)
timeline.add_modification(march_1_2026, 'add', world_etf_2)
print(f"-> {march_1_2026}: RECEIVE Loan Tranche 2 and CONSOLIDATE ETF holding.")

# --- 3. Run and Display Forecasts ---
if __name__ == "__main__":
    future_date_5_years = date.today() + relativedelta(years=+5)
    future_date_10_years = date.today() + relativedelta(years=+10)

    print("\n" + "="*50)
    print(f"      Forecasting for {future_date_5_years}")
    print("="*50)
    
    print("\n--- Scenario: Constant Growth ---")
    future_portfolio_5y = timeline.get_portfolio_at_date(future_date_5_years, scenario_name='constant_growth')
    print(future_portfolio_5y.summary())

    print("\n" + "="*50)
    print(f"      Forecasting for {future_date_10_years}")
    print("="*50)

    print("\n--- Scenario: Constant Growth ---")
    future_portfolio_10y = timeline.get_portfolio_at_date(future_date_10_years, scenario_name='constant_growth')
    print(future_portfolio_10y.summary())