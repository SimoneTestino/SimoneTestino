#!/usr/bin/env python3
"""
Plots the portfolio's currency exposure, using geography for ETFs.
"""

import sys
import os
from decimal import Decimal

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
plotters_dir = os.path.dirname(current_dir)
project_root = os.path.dirname(plotters_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Imports ---
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from moneyed import Money, get_currency

from FinancialClasses.Portfolio import Portfolio
from FinancialClasses.LiquidAssets import LiquidAssets

def plot_currency_exposure(portfolio: Portfolio, output_filename: str = "currency_exposure.png"):
    """
    Generates a bar chart of the portfolio's currency exposure.
    - Uses geography to determine currency for ETFs.
    - Excludes Illiquid assets.
    - Shows Debits as negative exposure.
    """
    print("--- Generating Currency Exposure Plot ---")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(script_dir, "PlotsSaved")
    os.makedirs(save_dir, exist_ok=True)
    full_output_path = os.path.join(save_dir, output_filename)

    # --- 1. Data Aggregation ---
    currency_data = {}
    converter = portfolio._converter

    # Mapping from asset geography to currency exposure
    geo_to_currency = {
        'USA': 'USD', 'Europe': 'EUR', 'China': 'CNY',
        'Global': 'USD', 'Emerging markets': 'USD', 'Else': 'EUR'
    }

    for asset in portfolio.assets:
        asset_class = getattr(asset, 'asset_class', '')
        # Skip Illiquid assets and future income streams
        if asset_class in ['illiquid', 'income_stream']:
            continue

        value_money = None
        if asset_class == 'market':
            value_money = getattr(asset, 'current_value', None) # Leveraged value for exposure
        elif asset_class == 'liquidity':
            value_money = getattr(asset, 'current_value', None)
        elif asset_class in ['credit', 'debit']:
            value_money = asset.total_outstanding(on_date=portfolio.valuation_date)
        
        if not value_money:
            continue
            
        # Determine the currency of exposure
        exposure_currency_code = value_money.currency.code
        if isinstance(asset, LiquidAssets) and asset.instrument_type == 'ETF':
            geography = getattr(asset, 'geography', 'Else')
            exposure_currency_code = geo_to_currency.get(geography, value_money.currency.code)
        
        if exposure_currency_code not in currency_data:
            currency_data[exposure_currency_code] = {'native_total': Decimal('0'), 'eur_total': Decimal('0')}

        # We need to convert the asset's value to its exposure currency if they differ
        # (e.g., a Global ETF traded in EUR has USD exposure)
        if value_money.currency.code != exposure_currency_code:
            native_value = converter.convert(value_money, exposure_currency_code).amount
        else:
            native_value = value_money.amount
        
        currency_data[exposure_currency_code]['native_total'] += native_value
        currency_data[exposure_currency_code]['eur_total'] += converter.convert(value_money, 'EUR').amount

    # --- 2. Data Preparation ---
    plot_data = []
    for code, values in currency_data.items():
        native_money = Money(values['native_total'], code)
        plot_data.append([code, values['eur_total'], native_money])

    df = pd.DataFrame(plot_data, columns=['Currency', 'Value (EUR)', 'Native Value'])
    df = df.sort_values(by='Value (EUR)', ascending=False)
    
    total_positive_exposure = df[df['Value (EUR)'] > 0]['Value (EUR)'].sum()
    if total_positive_exposure == 0:
        print("Total exposure is zero. Skipping plot.")
        return

    # --- 3. Print Key Values ---
    print("\nCurrency Exposure Summary (Leveraged):")
    print(f"Total Positive Exposure: €{total_positive_exposure:,.2f}")
    print("-" * 50)
    print(f"{'Currency':<10} | {'Value (EUR)':>15} | {'Native Value':>20}")
    print("-" * 50)
    for index, row in df.iterrows():
        print(f"{row['Currency']:<10} | {row['Value (EUR)']:>15,.2f} | {str(row['Native Value']):>20}")
    print("-" * 50)

    # --- 4. Plotting ---
    df_plot = df.astype({'Value (EUR)': float})
    total_exposure_float = float(total_positive_exposure)
    
    sns.set_style("whitegrid")
    plt.rc('font', family='sans-serif')
    fig, ax1 = plt.subplots(figsize=(10, 7))

    # Plot bars and add custom labels
    for index, row in df_plot.iterrows():
        color = '#b20710' if row['Value (EUR)'] < 0 else '#444444'
        ax1.bar(row['Currency'], row['Value (EUR)'], color=color)
        
        # Add the native value label
        height = row['Value (EUR)']
        offset = total_exposure_float * 0.015 if height > 0 else -total_exposure_float * 0.04
        label_text = f"{row['Native Value']}"
        ax1.text(row['Currency'], height + offset, label_text, ha='center', fontsize=9, weight='bold')

    # --- 5. Dual Y-Axis and Styling ---
    ax2 = ax1.twinx()
    min_val, max_val = ax1.get_ylim()
    ax2.set_ylim(min_val / total_exposure_float * 100, max_val / total_exposure_float * 100)
    ax2.yaxis.set_major_formatter(mticker.PercentFormatter())

    fig.suptitle('Portfolio Exposure by Currency', fontsize=16, weight='bold')
    ax1.set_title('ETF currency is based on geography; other assets on native currency', fontsize=10, style='italic')
    ax1.set_xlabel('Currency', fontsize=12)
    ax1.set_ylabel('Leveraged Value (€)', fontsize=12, color='#444444')
    ax2.set_ylabel('Percentage of Total Exposure', fontsize=12, color='#444444')
    ax1.grid(axis='x')
    ax2.grid(False)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    # --- 6. Save and Show ---
    plt.savefig(full_output_path, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved successfully as '{full_output_path}'")
    plt.show()

# --- Example Usage ---
if __name__ == '__main__':
    try:
        from Constants.ActualConstants import portfolio
        portfolio.update_all_market_values()
        plot_currency_exposure(portfolio)
    except ImportError:
        print("Could not import portfolio from Constants/ActualConstants.py")
        print("Please run this plotter via main.py")