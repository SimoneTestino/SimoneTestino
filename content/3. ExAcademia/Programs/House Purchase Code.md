---
draft: false
date: 2025-05-17
---
Taking into account the precious considerations exposed in [YT: Rent vs Buy](https://youtu.be/j4H9LL7A-nQ?si=Y_FRA7IpXWGG5A_K) by Ben Felix, I execute the following computations to determine the cases in which buying a house is going to be an advantage.

```Python
import matplotlib.pyplot as plt

import numpy as np

  

# =============================================================================

# CONFIGURATION CONSTANTS

# =============================================================================

  

# --- PROPERTY DETAILS ---

PRICE_PROPERTY = 18000

RESTRUCTURING_COSTS = [("unforeseen", 0)] # List of (description, cost)

  

# --- FINANCIAL PARAMETERS ---

MARKET_TAEG = 0.036 # Annual interest rate for a generic market loan

FIRST_HOME_TAEG = 0.04 # Annual interest rate for a first home mortgage

  

# --- RENTAL ASSUMPTIONS (for Scenario 2 and for user's own rent if buying) ---

USER_STUDY_RENT_MONTHS = 12 # How many months the user pays rent externally (e.g., while renovating or if S1 house is rented out initially)

USER_STUDY_MONTHLY_RENT_EXTERNAL = 300 # User's monthly rent paid to someone else

  

# --- NEW: PURCHASED HOUSE RENTAL INCOME DETAILS (SCENARIO 1, if applicable) ---

FIXED_MONTHLY_RENT_FROM_HOUSE_NET = 200 # Net monthly rent if house is rented out long-term

B_AND_B_INCOME_MONTHLY_SEASON_NET = 400 # Additional net monthly income from B&B during season

B_AND_B_INCOME_MONTHLY_OFF_SEASON_NET = 0 # Additional net monthly income from B&B off-season

SEASON_MONTHS = [6, 7, 8, 9] # Months considered "in season" (1=Jan, 12=Dec)

  

# --- INVESTMENT ASSUMPTIONS ---

ANNUAL_GROSS_INVESTMENT_RETURN = 0.10 # Gross annual return on invested capital

CAPITAL_GAINS_TAX_RATE = 0.26 # Tax rate on capital gains from investments (e.g., 26%)

  

# --- LOAN PRODUCT DETAILS ---

HOUSE_LOAN_MAX_CAPACITY = 10000 # Maximum amount that can be borrowed for the house

HOUSE_LOAN_PERCENTAGE_OF_PRICE = 0.80 # Percentage of PRICE_PROPERTY to be financed by loan (e.g., 80% LTV)

HOUSE_LOAN_DURATION_MONTHS = 120 # Duration of the house loan in months (e.g., 10 years)

INVESTMENT_LOAN_MAX_CAPACITY = 20000 # Maximum amount for a dedicated investment loan (Scenario 2)

INVESTMENT_LOAN_DURATION_MONTHS = 120 # Duration of the investment loan in months

MIN_FIRST_HOME_LOAN_AMOUNT = 30000 # Minimum loan amount for favorable first home TAEG

  

# --- PURCHASED HOUSE OPERATIONALS (SCENARIO 1) ---

ANNUAL_NOMINAL_HOUSE_APPRECIATION_RATE = 0.01 # Annual nominal appreciation rate of the house value

  

# --- PURCHASED HOUSE FIXED COSTS (SCENARIO 1) ---

IMU_ANNUAL_TAX = 300 # Annual property tax (IMU)

UTILITIES_MONTHLY_OWNER_OCCUPIED_OR_RENTED = 20 # Monthly utilities if owner-occupied or if owner pays while rented

  

# --- VALUATION & STARTING NET LIQUIDATION VALUE ---

RENOVATION_VALUE_ADD_FIXED = 0 # Fixed value added by renovation, beyond costs

ASSUME_CGT_ON_HOUSE_APPRECIATION_FOR_NLV = True # Apply capital gains tax to house appreciation for NLV calculation

STARTING_NET_LIQUIDATION_VALUE = 38000 # User's initial available capital

  

# =============================================================================

# HELPER FUNCTIONS

# =============================================================================

def calc_total_restruct(costs):

"""Calculates the sum of restructuring costs."""

return sum(cost for _, cost in costs)

  

def fv(principal, annual_rate, total_months):

"""Calculates future value of a principal."""

if total_months <= 0: return principal

if principal == 0: return 0

monthly_rate = annual_rate / 12

return principal * (1 + monthly_rate) ** total_months

  

def pmnt(principal, annual_rate, total_months):

"""Calculates the fixed monthly payment for a loan."""

if total_months <= 0 or principal == 0: return 0

if annual_rate == 0: return principal / total_months if total_months > 0 else 0

monthly_rate = annual_rate / 12

if abs(monthly_rate) < 1e-9: # Effectively zero rate

try:

return principal / total_months if total_months > 0 else 0

except ZeroDivisionError:

return 0

try:

payment = principal * (monthly_rate * (1 + monthly_rate)**total_months) / ((1 + monthly_rate)**total_months - 1)

except OverflowError:

payment = principal * monthly_rate

return payment

  

def balance(principal, annual_rate, total_months, months_passed):

"""Calculates the remaining balance of a loan after a certain number of months."""

if months_passed <= 0: return principal

if principal == 0: return 0

if months_passed >= total_months: return 0

  

payment_val = pmnt(principal, annual_rate, total_months)

monthly_rate = annual_rate / 12

  

if annual_rate == 0 or abs(monthly_rate) < 1e-9: # Effectively zero rate

return max(0, principal - payment_val * months_passed)

  

current_balance = principal * (1 + monthly_rate)**months_passed - \

payment_val * (((1 + monthly_rate)**months_passed - 1) / monthly_rate)

return max(0, current_balance)

  

# =============================================================================

# INITIAL SETUP

# =============================================================================

TOTAL_RESTRUCT = calc_total_restruct(RESTRUCTURING_COSTS)

TOTAL_HOUSE_COST_INITIAL = PRICE_PROPERTY + TOTAL_RESTRUCT

HOUSE_VALUE_AFTER_RENOVATION = TOTAL_HOUSE_COST_INITIAL + RENOVATION_VALUE_ADD_FIXED

  

# Scenario 1: Buy House

loan_amount_based_on_ltv_s1 = PRICE_PROPERTY * HOUSE_LOAN_PERCENTAGE_OF_PRICE

ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1 = min(loan_amount_based_on_ltv_s1, HOUSE_LOAN_MAX_CAPACITY)

  

effective_first_home_taeg_s1 = FIRST_HOME_TAEG

if ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1 > 0 and ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1 < MIN_FIRST_HOME_LOAN_AMOUNT:

print(f"WARNING: Scenario 1 House Loan (€{ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1:,.2f}) is below the typical minimum of €{MIN_FIRST_HOME_LOAN_AMOUNT:,.2f} for a first home loan.")

print(f" The assumed FIRST_HOME_TAEG of {FIRST_HOME_TAEG:.2%} might not be applicable and could be higher (e.g., closer to MARKET_TAEG of {MARKET_TAEG:.2%}).")

print(f" The simulation will proceed with {FIRST_HOME_TAEG:.2%}, but be aware of this assumption.")

  

cash_needed_from_pocket_s1 = (PRICE_PROPERTY - ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1) + TOTAL_RESTRUCT

cash_needed_from_pocket_s1 = max(0, cash_needed_from_pocket_s1)

  

invested_capital_s1_at_t0 = STARTING_NET_LIQUIDATION_VALUE - cash_needed_from_pocket_s1

  

# Scenario 2: Rent & Invest

INVESTMENT_PRINCIPAL_SCENARIO_2 = INVESTMENT_LOAN_MAX_CAPACITY

  

# =============================================================================

# CAPITAL EVOLUTION (NET LIQUIDATION VALUE & NET INVESTED CAPITAL)

# =============================================================================

COMPARISON_DURATION_MONTHS = max(HOUSE_LOAN_DURATION_MONTHS, INVESTMENT_LOAN_DURATION_MONTHS, USER_STUDY_RENT_MONTHS)

months_array = np.arange(COMPARISON_DURATION_MONTHS + 1)

  

nlv_s1 = np.zeros(len(months_array))

nlv_s2 = np.zeros(len(months_array))

nlv_benchmark = np.zeros(len(months_array))

  

net_invested_capital_s1_plot = np.zeros(len(months_array))

net_invested_capital_s2_plot = np.zeros(len(months_array))

  

# --- NLV and Net Invested Capital at t=0 ---

net_invested_capital_s1_plot[0] = invested_capital_s1_at_t0 if invested_capital_s1_at_t0 > 0 else 0

nlv_s1[0] = HOUSE_VALUE_AFTER_RENOVATION + net_invested_capital_s1_plot[0] - ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1

  

initial_rent_paid_s2_at_t0 = 0

if USER_STUDY_RENT_MONTHS > 0 :

initial_rent_paid_s2_at_t0 = USER_STUDY_MONTHLY_RENT_EXTERNAL

  

invested_capital_s2_at_t0_initial_part = STARTING_NET_LIQUIDATION_VALUE - initial_rent_paid_s2_at_t0

net_invested_capital_s2_initial_at_t0 = invested_capital_s2_at_t0_initial_part if invested_capital_s2_at_t0_initial_part > 0 else 0

net_invested_capital_s2_loan_funded_at_t0 = INVESTMENT_PRINCIPAL_SCENARIO_2

net_invested_capital_s2_plot[0] = net_invested_capital_s2_initial_at_t0 + net_invested_capital_s2_loan_funded_at_t0

nlv_s2[0] = net_invested_capital_s2_initial_at_t0

  

nlv_benchmark[0] = STARTING_NET_LIQUIDATION_VALUE

  

running_s1_invested_capital_main_gross = invested_capital_s1_at_t0

contributions_s1_invested_capital_main = max(0, invested_capital_s1_at_t0)

running_s1_reinvested_cashflow_gross = 0.0

contributions_s1_reinvested_cashflow = 0.0

s1_total_principal_deficits_covered = 0.0

s1_value_of_covered_deficits_compounded = 0.0

  

running_s2_invested_capital_initial_gross = invested_capital_s2_at_t0_initial_part

contributions_s2_invested_capital_initial = max(0, invested_capital_s2_at_t0_initial_part)

running_s2_invested_capital_loan_gross = INVESTMENT_PRINCIPAL_SCENARIO_2

contributions_s2_invested_capital_loan = max(0, INVESTMENT_PRINCIPAL_SCENARIO_2)

  

running_benchmark_capital_gross = STARTING_NET_LIQUIDATION_VALUE

contributions_benchmark_capital = STARTING_NET_LIQUIDATION_VALUE

initial_benchmark_rent_paid_at_t0 = 0

if USER_STUDY_RENT_MONTHS > 0 :

initial_benchmark_rent_paid_at_t0 = USER_STUDY_MONTHLY_RENT_EXTERNAL

running_benchmark_capital_gross -= initial_benchmark_rent_paid_at_t0

contributions_benchmark_capital = STARTING_NET_LIQUIDATION_VALUE - initial_benchmark_rent_paid_at_t0

  

cumulative_rent_paid_s2_for_printout = initial_rent_paid_s2_at_t0

monthly_imu_cost = IMU_ANNUAL_TAX / 12

monthly_investment_rate = ANNUAL_GROSS_INVESTMENT_RETURN / 12

monthly_house_appreciation_rate = ANNUAL_NOMINAL_HOUSE_APPRECIATION_RATE / 12

  

monthly_house_payment_s1 = pmnt(ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1, effective_first_home_taeg_s1, HOUSE_LOAN_DURATION_MONTHS)

monthly_investment_loan_payment_s2 = pmnt(INVESTMENT_PRINCIPAL_SCENARIO_2, MARKET_TAEG, INVESTMENT_LOAN_DURATION_MONTHS)

monthly_fixed_operational_costs_s1 = monthly_imu_cost + UTILITIES_MONTHLY_OWNER_OCCUPIED_OR_RENTED

  

s1_failed = False; s1_fail_idx = -1; s1_fail_value = np.nan

s2_failed = False; s2_fail_idx = -1; s2_fail_value = np.nan

s1_failure_threshold = -0.5 * ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1 if ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1 > 0 else -0.5 * STARTING_NET_LIQUIDATION_VALUE

s2_failure_threshold = -0.5 * INVESTMENT_PRINCIPAL_SCENARIO_2 if INVESTMENT_PRINCIPAL_SCENARIO_2 > 0 else -0.5 * STARTING_NET_LIQUIDATION_VALUE

  

final_s1_net_liq_house_value = HOUSE_VALUE_AFTER_RENOVATION

if ASSUME_CGT_ON_HOUSE_APPRECIATION_FOR_NLV and RENOVATION_VALUE_ADD_FIXED > 0 :

final_s1_net_liq_house_value -= max(0, RENOVATION_VALUE_ADD_FIXED) * CAPITAL_GAINS_TAX_RATE

elif not ASSUME_CGT_ON_HOUSE_APPRECIATION_FOR_NLV:

final_s1_net_liq_house_value = HOUSE_VALUE_AFTER_RENOVATION

  

final_s1_net_liq_invested_main = net_invested_capital_s1_plot[0]

final_s1_net_liq_reinvested_cf = 0.0

final_s1_house_loan_liability = ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1

  

final_s2_net_liq_invested_initial = net_invested_capital_s2_initial_at_t0

final_s2_net_liq_invested_loan = net_invested_capital_s2_loan_funded_at_t0

final_s2_investment_loan_liability = INVESTMENT_PRINCIPAL_SCENARIO_2

  

for m_idx, m_val in enumerate(months_array):

if m_val == 0:

if not s1_failed and nlv_s1[0] < s1_failure_threshold:

s1_failed = True; s1_fail_idx = 0; s1_fail_value = nlv_s1[0]

if not s2_failed and nlv_s2[0] < s2_failure_threshold:

s2_failed = True; s2_fail_idx = 0; s2_fail_value = nlv_s2[0]

continue

  

# --- SCENARIO 1: Buy & Manage ---

if s1_failed:

nlv_s1[m_idx] = np.nan

net_invested_capital_s1_plot[m_idx] = np.nan

else:

if running_s1_invested_capital_main_gross > 0:

running_s1_invested_capital_main_gross *= (1 + monthly_investment_rate)

if running_s1_reinvested_cashflow_gross > 0:

running_s1_reinvested_cashflow_gross *= (1 + monthly_investment_rate)

if s1_value_of_covered_deficits_compounded > 0:

s1_value_of_covered_deficits_compounded *= (1 + monthly_investment_rate)

  

current_gross_house_value_s1 = fv(HOUSE_VALUE_AFTER_RENOVATION, ANNUAL_NOMINAL_HOUSE_APPRECIATION_RATE, m_val)

house_gain_s1 = current_gross_house_value_s1 - HOUSE_VALUE_AFTER_RENOVATION

house_appreciation_cgt_s1 = 0

if ASSUME_CGT_ON_HOUSE_APPRECIATION_FOR_NLV:

house_appreciation_cgt_s1 = max(0, house_gain_s1) * CAPITAL_GAINS_TAX_RATE

net_liquidated_house_value_s1 = current_gross_house_value_s1 - house_appreciation_cgt_s1

final_s1_net_liq_house_value = net_liquidated_house_value_s1

  

current_month_of_year = (m_val - 1) % 12 + 1

bnb_income_this_month_net = B_AND_B_INCOME_MONTHLY_SEASON_NET if current_month_of_year in SEASON_MONTHS else B_AND_B_INCOME_MONTHLY_OFF_SEASON_NET

positive_cash_inflow_s1 = FIXED_MONTHLY_RENT_FROM_HOUSE_NET + bnb_income_this_month_net

  

user_external_rent_payment_s1 = 0 # MODIFICATION: User lives in the house, no external rent

  

total_monthly_outgoings_s1 = monthly_fixed_operational_costs_s1 + monthly_house_payment_s1 + user_external_rent_payment_s1

net_monthly_cashflow_s1 = positive_cash_inflow_s1 - total_monthly_outgoings_s1

  

if net_monthly_cashflow_s1 > 0:

running_s1_reinvested_cashflow_gross += net_monthly_cashflow_s1

contributions_s1_reinvested_cashflow += net_monthly_cashflow_s1

elif net_monthly_cashflow_s1 < 0:

deficit_to_cover = abs(net_monthly_cashflow_s1)

s1_total_principal_deficits_covered += deficit_to_cover

s1_value_of_covered_deficits_compounded += deficit_to_cover

  

draw_from_main = min(deficit_to_cover, running_s1_invested_capital_main_gross)

running_s1_invested_capital_main_gross -= draw_from_main

deficit_to_cover -= draw_from_main

  

if deficit_to_cover > 0:

draw_from_reinvested = min(deficit_to_cover, running_s1_reinvested_cashflow_gross)

running_s1_reinvested_cashflow_gross -= draw_from_reinvested

running_s1_invested_capital_main_gross = max(0, running_s1_invested_capital_main_gross)

running_s1_reinvested_cashflow_gross = max(0, running_s1_reinvested_cashflow_gross)

  

s1_main_capital_gain = max(0, running_s1_invested_capital_main_gross - contributions_s1_invested_capital_main)

s1_main_capital_cgt = s1_main_capital_gain * CAPITAL_GAINS_TAX_RATE

net_liquidated_s1_invested_main = running_s1_invested_capital_main_gross - s1_main_capital_cgt

final_s1_net_liq_invested_main = net_liquidated_s1_invested_main

  

s1_reinvested_cf_gain = max(0, running_s1_reinvested_cashflow_gross - contributions_s1_reinvested_cashflow)

s1_reinvested_cf_cgt = s1_reinvested_cf_gain * CAPITAL_GAINS_TAX_RATE

net_liquidated_s1_reinvested_cf = running_s1_reinvested_cashflow_gross - s1_reinvested_cf_cgt

final_s1_net_liq_reinvested_cf = net_liquidated_s1_reinvested_cf

  

net_invested_capital_s1_plot[m_idx] = net_liquidated_s1_invested_main + net_liquidated_s1_reinvested_cf

  

house_loan_liability_s1 = balance(ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1, effective_first_home_taeg_s1, HOUSE_LOAN_DURATION_MONTHS, m_val)

final_s1_house_loan_liability = house_loan_liability_s1

  

nlv_s1[m_idx] = net_liquidated_house_value_s1 + net_invested_capital_s1_plot[m_idx] - house_loan_liability_s1

  

if nlv_s1[m_idx] < s1_failure_threshold:

s1_failed = True; s1_fail_idx = m_idx; s1_fail_value = nlv_s1[m_idx]

final_s1_net_liq_house_value = net_liquidated_house_value_s1

final_s1_net_liq_invested_main = net_liquidated_s1_invested_main

final_s1_net_liq_reinvested_cf = net_liquidated_s1_reinvested_cf

final_s1_house_loan_liability = house_loan_liability_s1

  

# --- SCENARIO 2: Rent & Invest ---

if s2_failed:

nlv_s2[m_idx] = np.nan

net_invested_capital_s2_plot[m_idx] = np.nan

else:

if running_s2_invested_capital_initial_gross > 0:

running_s2_invested_capital_initial_gross *= (1 + monthly_investment_rate)

if running_s2_invested_capital_loan_gross > 0:

running_s2_invested_capital_loan_gross *= (1 + monthly_investment_rate)

  

rent_payment_s2_this_month = 0

if m_val <= USER_STUDY_RENT_MONTHS :

if m_val > 0:

if not (m_val == 1 and initial_rent_paid_s2_at_t0 > 0) :

rent_payment_s2_this_month = USER_STUDY_MONTHLY_RENT_EXTERNAL

cumulative_rent_paid_s2_for_printout += rent_payment_s2_this_month

  

payment_due_for_loan_s2 = monthly_investment_loan_payment_s2 if INVESTMENT_PRINCIPAL_SCENARIO_2 > 0 else 0

total_outgoings_s2 = rent_payment_s2_this_month + payment_due_for_loan_s2

  

draw_from_initial_s2 = min(total_outgoings_s2, running_s2_invested_capital_initial_gross)

running_s2_invested_capital_initial_gross -= draw_from_initial_s2

total_outgoings_s2 -= draw_from_initial_s2

  

if total_outgoings_s2 > 0:

draw_from_loan_funded_s2 = min(total_outgoings_s2, running_s2_invested_capital_loan_gross)

running_s2_invested_capital_loan_gross -= draw_from_loan_funded_s2

running_s2_invested_capital_initial_gross = max(0, running_s2_invested_capital_initial_gross)

running_s2_invested_capital_loan_gross = max(0, running_s2_invested_capital_loan_gross)

  

s2_initial_capital_gain = max(0, running_s2_invested_capital_initial_gross - contributions_s2_invested_capital_initial)

s2_initial_capital_cgt = s2_initial_capital_gain * CAPITAL_GAINS_TAX_RATE

net_liquidated_s2_invested_initial = running_s2_invested_capital_initial_gross - s2_initial_capital_cgt

final_s2_net_liq_invested_initial = net_liquidated_s2_invested_initial

  

s2_loan_capital_gain = max(0, running_s2_invested_capital_loan_gross - contributions_s2_invested_capital_loan)

s2_loan_capital_cgt = s2_loan_capital_gain * CAPITAL_GAINS_TAX_RATE

net_liquidated_s2_invested_loan = running_s2_invested_capital_loan_gross - s2_loan_capital_cgt

final_s2_net_liq_invested_loan = net_liquidated_s2_invested_loan

  

net_invested_capital_s2_plot[m_idx] = net_liquidated_s2_invested_initial + net_liquidated_s2_invested_loan

  

investment_loan_liability_s2 = balance(INVESTMENT_PRINCIPAL_SCENARIO_2, MARKET_TAEG, INVESTMENT_LOAN_DURATION_MONTHS, m_val)

final_s2_investment_loan_liability = investment_loan_liability_s2

  

nlv_s2[m_idx] = net_invested_capital_s2_plot[m_idx] - investment_loan_liability_s2

  

if nlv_s2[m_idx] < s2_failure_threshold:

s2_failed = True; s2_fail_idx = m_idx; s2_fail_value = nlv_s2[m_idx]

final_s2_net_liq_invested_initial = net_liquidated_s2_invested_initial

final_s2_net_liq_invested_loan = net_liquidated_s2_invested_loan

final_s2_investment_loan_liability = investment_loan_liability_s2

  

# --- BENCHMARK: Initial Capital Invested Externally ---

if running_benchmark_capital_gross > 0:

running_benchmark_capital_gross *= (1 + monthly_investment_rate)

  

benchmark_rent_payment_this_month = 0

if m_val <= USER_STUDY_RENT_MONTHS :

if not (m_val == 1 and initial_benchmark_rent_paid_at_t0 > 0 and USER_STUDY_RENT_MONTHS >=1):

benchmark_rent_payment_this_month = USER_STUDY_MONTHLY_RENT_EXTERNAL

  

running_benchmark_capital_gross -= benchmark_rent_payment_this_month

running_benchmark_capital_gross = max(0, running_benchmark_capital_gross)

  

benchmark_gain = max(0, running_benchmark_capital_gross - contributions_benchmark_capital)

benchmark_cgt = benchmark_gain * CAPITAL_GAINS_TAX_RATE

nlv_benchmark[m_idx] = running_benchmark_capital_gross - benchmark_cgt

  

# =============================================================================

# FINAL SNAPSHOT & ANALYSIS

# =============================================================================

print(f"\n--- End-of-Period Financial Snapshot (after up to {COMPARISON_DURATION_MONTHS/12:.1f} years) ---")

  

# --- Scenario 1 Output ---

print("\nScenario 1 (Buy House & Manage - User lives in the house):") # Clarification

print(f" Starting NLV contribution: €{STARTING_NET_LIQUIDATION_VALUE:,.2f}")

print(f" Initial cash from pocket for house & restructure: €{cash_needed_from_pocket_s1:,.2f}")

print(f" Initial capital invested (after house costs, net at t0): €{net_invested_capital_s1_plot[0]:,.2f}")

  

if s1_failed and s1_fail_idx >= 0:

print(f" Net Liquidated Final House Value (at failure, after CGT if appl.): €{final_s1_net_liq_house_value:,.2f}")

print(f" Net Liquidated Main Invested Capital (at failure, after CGT, draws): €{final_s1_net_liq_invested_main:,.2f}")

print(f" Net Liquidated Reinvested Cash Flows (at failure, after CGT, draws): €{final_s1_net_liq_reinvested_cf:,.2f}")

print(f" Total Final Net Invested Capital (at failure): €{final_s1_net_liq_invested_main + final_s1_net_liq_reinvested_cf:,.2f}")

print(f" Remaining House Loan Liability (at failure): €{final_s1_house_loan_liability:,.2f}")

print(f" SCENARIO 1 FAILED at month {s1_fail_idx} (Year {s1_fail_idx/12:.1f}) with NLV: €{s1_fail_value:,.2f}")

print(f" Final Net Liquidation Value (at failure): €{s1_fail_value:,.2f}")

else:

final_net_invested_s1 = net_invested_capital_s1_plot[COMPARISON_DURATION_MONTHS] if COMPARISON_DURATION_MONTHS < len(net_invested_capital_s1_plot) else net_invested_capital_s1_plot[-1]

final_nlv_s1 = nlv_s1[COMPARISON_DURATION_MONTHS] if COMPARISON_DURATION_MONTHS < len(nlv_s1) else nlv_s1[-1]

print(f" Net Liquidated Final House Value (after CGT if appl.): €{final_s1_net_liq_house_value:,.2f}")

print(f" Net Liquidated Main Invested Capital (after CGT, draws): €{final_s1_net_liq_invested_main:,.2f}")

print(f" Net Liquidated Reinvested Cash Flows (after CGT, draws): €{final_s1_net_liq_reinvested_cf:,.2f}")

print(f" Total Final Net Invested Capital (Scenario 1): €{final_net_invested_s1:,.2f}")

print(f" Remaining House Loan Liability: €{final_s1_house_loan_liability:,.2f}")

print(f" Final Net Liquidation Value (Scenario 1): €{final_nlv_s1:,.2f}")

  
  

print("\n -- Scenario 1: Detailed Loan Analysis (House Purchase) --")

print(f" Loan Principal: €{ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1:,.2f}")

print(f" Annual Interest Rate (TAEG): {effective_first_home_taeg_s1:.2%}")

print(f" Loan Duration: {HOUSE_LOAN_DURATION_MONTHS} months ({HOUSE_LOAN_DURATION_MONTHS/12:.1f} years)")

print(f" Calculated Fixed Monthly Payment: €{monthly_house_payment_s1:,.2f}")

if ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1 > 0 and HOUSE_LOAN_DURATION_MONTHS > 0 :

total_paid_s1_loan_full_term = monthly_house_payment_s1 * HOUSE_LOAN_DURATION_MONTHS

total_interest_s1_loan_full_term = total_paid_s1_loan_full_term - ACTUAL_HOUSE_LOAN_TAKEN_SCENARIO_1

print(f" Total Paid Over Full Loan Life (if held to term): €{total_paid_s1_loan_full_term:,.2f}")

print(f" Total Interest Paid Over Full Loan Life (if held to term): €{total_interest_s1_loan_full_term:,.2f}")

else:

print(f" No loan taken or zero duration for house purchase.")

print(f" Remaining Loan Liability (at end of simulation period of {COMPARISON_DURATION_MONTHS/12:.1f} years): €{final_s1_house_loan_liability:,.2f}")

  
  

print("\n -- Scenario 1: Estimated Monthly Cashflow Breakdown (User lives in the house) --")

print(f" Income (from House, per month - e.g., from a lodger/partial rental):")

print(f" Fixed Net Monthly Rent: €{FIXED_MONTHLY_RENT_FROM_HOUSE_NET:,.2f}")

print(f" Net B&B Income (In-Season, e.g., Months {SEASON_MONTHS}): €{B_AND_B_INCOME_MONTHLY_SEASON_NET:,.2f}")

print(f" Net B&B Income (Off-Season): €{B_AND_B_INCOME_MONTHLY_OFF_SEASON_NET:,.2f}")

print(f" Expenses (per month):")

print(f" House Fixed Operational (IMU, Utilities): €{monthly_fixed_operational_costs_s1:,.2f}")

print(f" House Loan Payment: €{monthly_house_payment_s1:,.2f}")

print(f" (User lives in the purchased house and does not pay separate external rent in this scenario.)")

  

print(f" Illustrative Net Monthly Cashflow (S1):")

s1_cf_in_season = (FIXED_MONTHLY_RENT_FROM_HOUSE_NET + B_AND_B_INCOME_MONTHLY_SEASON_NET) - (monthly_fixed_operational_costs_s1 + monthly_house_payment_s1)

s1_cf_off_season = (FIXED_MONTHLY_RENT_FROM_HOUSE_NET + B_AND_B_INCOME_MONTHLY_OFF_SEASON_NET) - (monthly_fixed_operational_costs_s1 + monthly_house_payment_s1)

  

print(f" In-Season: €{s1_cf_in_season:,.2f}")

print(f" Off-Season: €{s1_cf_off_season:,.2f}")

print(f" (Note: Negative cashflows are covered by drawing from invested capital in the simulation.)")

  
  

print("\n -- Scenario 1: Analysis of Cumulative Net Cash Flows Impact --")

s1_net_profit_on_reinvested_cashflows = final_s1_net_liq_reinvested_cf - contributions_s1_reinvested_cashflow

s1_foregone_growth_on_deficits = s1_value_of_covered_deficits_compounded - s1_total_principal_deficits_covered

print(f" Total principal from positive monthly cash flows reinvested: €{contributions_s1_reinvested_cashflow:,.2f}")

print(f" Net profit generated by these reinvested cash flows (after CGT): €{s1_net_profit_on_reinvested_cashflows:,.2f}")

print(f" Total principal deficits covered by drawing from capital: €{s1_total_principal_deficits_covered:,.2f}")

print(f" Estimated foregone investment growth on these covered deficits (compounded at {ANNUAL_GROSS_INVESTMENT_RETURN:.2%}): €{s1_foregone_growth_on_deficits:,.2f}")

  
  

# --- Scenario 2 Output ---

print("\nScenario 2 (Rent & Invest via Loan):")

print(f" Starting NLV contribution: €{STARTING_NET_LIQUIDATION_VALUE:,.2f}")

if s2_failed and s2_fail_idx >= 0:

print(f" Net Liquidated Initial Invested Capital (at failure, after rent, CGT, draws): €{final_s2_net_liq_invested_initial:,.2f}")

print(f" Net Liquidated Loan-Funded Investment (at failure, after CGT, draws): €{final_s2_net_liq_invested_loan:,.2f}")

print(f" Total Final Net Invested Capital (at failure): €{final_s2_net_liq_invested_initial + final_s2_net_liq_invested_loan:,.2f}")

print(f" Remaining Investment Loan Liability (at failure): €{final_s2_investment_loan_liability:,.2f}")

print(f" SCENARIO 2 FAILED at month {s2_fail_idx} (Year {s2_fail_idx/12:.1f}) with NLV: €{s2_fail_value:,.2f}")

print(f" Final Net Liquidation Value (at failure): €{s2_fail_value:,.2f}")

else:

final_net_invested_s2 = net_invested_capital_s2_plot[COMPARISON_DURATION_MONTHS] if COMPARISON_DURATION_MONTHS < len(net_invested_capital_s2_plot) else net_invested_capital_s2_plot[-1]

final_nlv_s2 = nlv_s2[COMPARISON_DURATION_MONTHS] if COMPARISON_DURATION_MONTHS < len(nlv_s2) else nlv_s2[-1]

print(f" Net Liquidated Initial Invested Capital (after rent, CGT, draws): €{final_s2_net_liq_invested_initial:,.2f}")

print(f" Net Liquidated Loan-Funded Investment (after CGT, draws): €{final_s2_net_liq_invested_loan:,.2f}")

print(f" Total Final Net Invested Capital (Scenario 2): €{final_net_invested_s2:,.2f}")

print(f" Remaining Investment Loan Liability: €{final_s2_investment_loan_liability:,.2f}")

print(f" Final Net Liquidation Value (Scenario 2): €{final_nlv_s2:,.2f}")

print(f" Total Rent Paid by User (during first {USER_STUDY_RENT_MONTHS} months): €{cumulative_rent_paid_s2_for_printout:,.2f}")

  
  

print("\n -- Scenario 2: Detailed Loan Analysis (Investment Loan) --")

print(f" Loan Principal: €{INVESTMENT_PRINCIPAL_SCENARIO_2:,.2f}")

print(f" Annual Interest Rate (TAEG): {MARKET_TAEG:.2%}")

print(f" Loan Duration: {INVESTMENT_LOAN_DURATION_MONTHS} months ({INVESTMENT_LOAN_DURATION_MONTHS/12:.1f} years)")

print(f" Calculated Fixed Monthly Payment: €{monthly_investment_loan_payment_s2:,.2f}")

if INVESTMENT_PRINCIPAL_SCENARIO_2 > 0 and INVESTMENT_LOAN_DURATION_MONTHS > 0:

total_paid_s2_loan_full_term = monthly_investment_loan_payment_s2 * INVESTMENT_LOAN_DURATION_MONTHS

total_interest_s2_loan_full_term = total_paid_s2_loan_full_term - INVESTMENT_PRINCIPAL_SCENARIO_2

print(f" Total Paid Over Full Loan Life (if held to term): €{total_paid_s2_loan_full_term:,.2f}")

print(f" Total Interest Paid Over Full Loan Life (if held to term): €{total_interest_s2_loan_full_term:,.2f}")

else:

print(f" No investment loan taken or zero duration.")

print(f" Remaining Loan Liability (at end of simulation period of {COMPARISON_DURATION_MONTHS/12:.1f} years): €{final_s2_investment_loan_liability:,.2f}")

  
  

print("\n -- Scenario 2: Estimated Monthly Outgoings Breakdown --")

print(f" Primary Outgoings (per month, covered by invested capital):")

if USER_STUDY_RENT_MONTHS > 0:

print(f" User's External Rent (first {USER_STUDY_RENT_MONTHS} months): €{USER_STUDY_MONTHLY_RENT_EXTERNAL:,.2f}")

if monthly_investment_loan_payment_s2 > 0:

print(f" Investment Loan Payment: €{monthly_investment_loan_payment_s2:,.2f}")

  

print(f" Illustrative Net Monthly Outgoings (S2, covered by drawing from investments):")

s2_outgoings_rent_period = (USER_STUDY_MONTHLY_RENT_EXTERNAL if USER_STUDY_RENT_MONTHS > 0 else 0) + monthly_investment_loan_payment_s2

s2_outgoings_post_rent_period = monthly_investment_loan_payment_s2

  

if USER_STUDY_RENT_MONTHS > 0:

print(f" During external rent period (first {USER_STUDY_RENT_MONTHS} months): €{s2_outgoings_rent_period:,.2f}")

if monthly_investment_loan_payment_s2 > 0 :

print(f" After external rent period (loan payment only, if applicable): €{s2_outgoings_post_rent_period:,.2f}")

elif monthly_investment_loan_payment_s2 > 0 :

print(f" Monthly (loan payment only): €{s2_outgoings_post_rent_period:,.2f}")

else:

print(f" No significant regular outgoings defined for S2 (rent/loan).")

print(f" (Note: These outgoings are covered by liquidating invested capital. Goal is for investment growth to outpace these costs.)")

  
  

# --- Benchmark Output ---

print("\nBenchmark (Initial Capital Invested, Paying External Rent if applicable):")

final_nlv_benchmark_idx = COMPARISON_DURATION_MONTHS if COMPARISON_DURATION_MONTHS < len(nlv_benchmark) else -1

final_nlv_benchmark = nlv_benchmark[final_nlv_benchmark_idx]

print(f" Final Net Liquidation Value (Benchmark): €{final_nlv_benchmark:,.2f}")

total_rent_paid_benchmark = 0

if USER_STUDY_RENT_MONTHS > 0:

num_rent_months_in_benchmark = min(USER_STUDY_RENT_MONTHS, COMPARISON_DURATION_MONTHS)

# Rent is paid at t=0 for the first month, and then for subsequent months up to USER_STUDY_RENT_MONTHS

total_rent_paid_benchmark = initial_benchmark_rent_paid_at_t0 # Rent for month 1 (paid at t=0)

if num_rent_months_in_benchmark > 1:

total_rent_paid_benchmark += USER_STUDY_MONTHLY_RENT_EXTERNAL * (num_rent_months_in_benchmark -1)

  

print(f" Estimated Total Rent Paid by User (Benchmark, up to {num_rent_months_in_benchmark} months): €{total_rent_paid_benchmark:,.2f}")

  
  

# =============================================================================

# PLOTTING

# =============================================================================

plt.style.use('seaborn-v0_8-whitegrid')

fig1, ax1 = plt.subplots(figsize=(14, 8))

years_array_plot = months_array / 12

  

s1_nlv_label = 'S1: Buy House (NLV)'

s1_ic_label = 'S1: Invested Capital (Net)'

if s1_failed: s1_nlv_label += ' (Failed)'; s1_ic_label += ' (Failed)'

ax1.plot(years_array_plot, nlv_s1, label=s1_nlv_label, color='red', linewidth=2, linestyle='-')

ax1.plot(years_array_plot, net_invested_capital_s1_plot, label=s1_ic_label, color='red', linewidth=1.5, linestyle='--')

if s1_failed and s1_fail_idx >= 0:

ax1.plot(years_array_plot[s1_fail_idx], s1_fail_value, 'rx', markersize=10, markeredgewidth=2, zorder=5, label='S1 Fail Point')

  

s2_nlv_label = 'S2: Rent & Invest (NLV)'

s2_ic_label = 'S2: Invested Capital (Net)'

if s2_failed: s2_nlv_label += ' (Failed)'; s2_ic_label += ' (Failed)'

ax1.plot(years_array_plot, nlv_s2, label=s2_nlv_label, color='black', linewidth=2, linestyle='-')

ax1.plot(years_array_plot, net_invested_capital_s2_plot, label=s2_ic_label, color='black', linewidth=1.5, linestyle='--')

if s2_failed and s2_fail_idx >= 0:

ax1.plot(years_array_plot[s2_fail_idx], s2_fail_value, 'kx', markersize=10, markeredgewidth=2, zorder=5, label='S2 Fail Point')

  

benchmark_label = f'Benchmark: Initial Capital Invested (NLV, {ANNUAL_GROSS_INVESTMENT_RETURN:.1%}, pays rent if applicable)'

ax1.plot(years_array_plot, nlv_benchmark, label=benchmark_label, color='blue', linestyle='-', linewidth=2)

  

ax1.set_xlabel("Years", fontsize=12)

ax1.set_ylabel("Value (EUR)", fontsize=12)

ax1.set_title("Capital Evolution: Buy vs. Rent & Invest", fontsize=14, fontweight='bold')

ax1.legend(loc='best', fontsize='medium')

ax1.grid(True, which='both', linestyle=':', linewidth=0.7)

ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

  

min_nlv_overall = np.nanmin([np.nanmin(nlv_s1) if not np.all(np.isnan(nlv_s1)) else np.inf,

np.nanmin(nlv_s2) if not np.all(np.isnan(nlv_s2)) else np.inf,

np.nanmin(nlv_benchmark) if not np.all(np.isnan(nlv_benchmark)) else np.inf])

  

if min_nlv_overall == np.inf: # all were nan or empty

min_nlv_overall = 0

  

if min_nlv_overall >= 0 :

ax1.set_ylim(bottom=0)

else:

ax1.set_ylim(bottom=min_nlv_overall * 1.1)

  

ax1.tick_params(axis='both', which='major', labelsize=10)

  

plt.tight_layout()

plt.show()

print("\n--- Important Non-Quantifiable Considerations ---")

  

final_comment = """

  

Beyond the numbers, purchasing this particular house offers several advantages

  

that are more challenging to quantify. Firstly, it could provide a stable base

  

for the 'Luna project', which might benefit significantly from a dedicated physical space.

  

Secondly, owning a home that can be personalised to one's tastes, situated in a

  

location with a strong and supportive social network, would undoubtedly enhance

  

the quality of life. Lastly, it presents a valuable opportunity for learning new skills

  

through renovation and provides a secure, personal space for storing belongings,

  

offering independence from reliance on others for such needs.

  

"""

  

print(final_comment)
```