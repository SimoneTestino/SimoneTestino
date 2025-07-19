print("Actual Contants initialized successfully.")
from datetime import date, timedelta
from moneyed import Money
from decimal import Decimal
from FinancialClasses.Liquidity import Liquidity
from FinancialClasses.Credit import Credit
from FinancialClasses.Debit import Debit
from FinancialClasses.LiquidAssets import LiquidAssets
from FinancialClasses.Portfolio import Portfolio
import warnings

manual_rates = {
    ('EUR', 'USD'): Decimal('1.1658'),  # 1 EUR ≈ 1.1658 USD :contentReference[oaicite:1]{index=1}
    ('USD', 'EUR'): Decimal('0.8577'),  # 1 USD ≈ 0.8577 EUR (inverse of above)

    ('EUR', 'CHF'): Decimal('0.9334'),  # 1 EUR ≈ 0.9334 CHF :contentReference[oaicite:2]{index=2}
    ('CHF', 'EUR'): Decimal('1.0714'),  # 1 CHF ≈ 1.0714 EUR (inverse)

    ('USD', 'CHF'): Decimal('0.8035'),  # 1 USD ≈ 0.8035 CHF :contentReference[oaicite:3]{index=3}
    ('CHF', 'USD'): Decimal('1.2456'),  # 1 CHF ≈ 1.2456 USD (inverse)
}

# Valuation and repayment dates
valuation_date = date(2025, 7, 15)
repayment_date = valuation_date + timedelta(days=7)

# 1. Liquidity: 30 CHF in cash
cash_chf = Liquidity(
    name="Cash (CHF)",
    amount=Money(30, "CHF"),
    storage="Wallet",
    description="Spare Swiss francs",
    acquisition_date=date(2025, 7, 1),
    acquisition_origin="Personal"
)

# 2. Liquidity: 80 EUR in cash
cash_eur = Liquidity(
    name="Cash (EUR)",
    amount=Money(80, "EUR"),
    storage="Wallet",
    description="Spare euros",
    acquisition_date=date(2025, 7, 1),
    acquisition_origin="Personal"
)

# 3. Liquidity: 5 187 EUR in bank account
bank_eur = Liquidity(
    name="ISP Bank Account",
    amount=Money(5929, "EUR"),
    storage="Bank Account",
    description="Checking account balance",
    acquisition_date=date(2025, 7, 1),
    acquisition_origin="Monthly Salary"
)

# 4. Debit: €1 400 fine owed to Lieven De Key
debit_fine = Debit(
    creditor="Lieven De Key",
    principal=Money(1400, "EUR"),
    debit_type="planned",
    interest_rate=0.00,
    repayment_schedule=[(repayment_date, Money(1400, "EUR"))]
)

# 5. Credit: €1 300 deposit owed back to you
credit_deposit = Credit(
    debtor="Lieven De Key",
    principal=Money(1300, "EUR"),
    credit_type="planned",
    interest_rate=0.00,
    repayment_schedule=[(date(2025, 9, 1), Money(1300, "EUR"))]
)

# 6. Conditional credit: 80 CHF deposit from SBB
reka = Credit(
    debtor="SBB",
    principal=Money(80, "CHF"),
    credit_type="conditional",
    interest_rate=0.00
)

# 7. China ETF
china_etf = LiquidAssets(
    name="iShares MSCI China A UCITS ETF USD (Acc)",
    ticker="36BZ.DE",
    quantity=1000,
    purchase_date=date(2025, 7, 1),
    instrument_type="ETF",
    etf_subtype="stocks",
    leverage=1.0,
    geography="China",
    isin="IE00BQT3WG13",
    price_checks_input=[(valuation_date, Money(4.12, "EUR"))]
)
china_etf.update_market_value()

# 8. MSCI USA 2× Leveraged ETF
cl2_etf = LiquidAssets(
    name="MSCI USA 2x Leveraged ETF",
    ticker="CL2.DE",
    quantity=360,
    purchase_date=date(2025, 7, 1),
    instrument_type="ETF",
    etf_subtype="stocks",
    leverage=2.0,
    geography="USA",
    isin="FR0010755611",
    price_checks_input=[(valuation_date, Money(21.30, "EUR"))]
)
cl2_etf.update_market_value()

# 9. Alibaba Group Holding Ltd
baba = LiquidAssets(
    name="Alibaba Group Holding Ltd",
    ticker="BABA",
    quantity=50,
    purchase_date=date(2025, 7, 1),
    instrument_type="stock",
    leverage=1.0,
    geography="China",
    price_checks_input=[(valuation_date, Money(116.26, "USD"))]
)
baba.update_market_value()

# 10. Baidu Inc
bidu = LiquidAssets(
    name="Baidu Inc",
    ticker="BIDU",
    quantity=45,
    purchase_date=date(2025, 7, 1),
    instrument_type="stock",
    leverage=1.0,
    geography="China",
    price_checks_input=[(valuation_date, Money(89.62, "USD"))]
)
bidu.update_market_value()

# 11. Intercos Group (Borsa Italiana)
#icga = LiquidAssets(
#    name="Intercos Group",
#    ticker="ICGA.MU",
#    quantity=710,
#    purchase_date=date(2025, 7, 1),
#    instrument_type="stock",
#    leverage=1.0,
#    geography="Europe",
#    isin="IE00BJ5JPG56",
#    price_checks_input=[(valuation_date, Money(4.88, "EUR"))]
#)
#icga.update_market_value()

# 12. ZPRV (Borsa Italiana)
zprv = LiquidAssets(
    name="ZPRV",
    ticker="ZPRV.DE",
    quantity=51,
    purchase_date=date(2025, 7, 1),
    instrument_type="stock",
    leverage=1.0,
    geography="Europe",
    isin="IE00BSPLC413",
    price_checks_input=[(valuation_date, Money(59.78, "EUR"))]
)
zprv.update_market_value()

# 13. Nike Inc
nke = LiquidAssets(
    name="Nike Inc",
    ticker="NKE",
    quantity=30,
    purchase_date=date(2025, 7, 1),
    instrument_type="stock",
    leverage=1.0,
    geography="USA",
    price_checks_input=[(valuation_date, Money(71.83, "USD"))]
)
nke.update_market_value()

# Build portfolio and add all assets
portfolio = Portfolio(valuation_date=valuation_date)
for asset in (
    cash_chf, cash_eur, bank_eur,
    debit_fine, credit_deposit, reka,
    china_etf, cl2_etf,
    baba, bidu, zprv, nke
):
    portfolio.add_asset(asset)

# Print portfolio summary
print(portfolio.summary())

print("ActualConstants module loaded successfully.")