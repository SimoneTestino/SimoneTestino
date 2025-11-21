#!/usr/bin/env python3
"""
Plots the portfolio's exposure by asset class, with a stacked bar for leverage.
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
from datetime import date
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from moneyed import Money, EUR

from FinancialClasses.Portfolio import Portfolio
from FinancialClasses.LiquidAssets import LiquidAssets

def plot_asset_class_exposure(portfolio: Portfolio, output_filename: str = "asset_class_exposure.png"):
    """
    Generates and saves a bar chart of portfolio exposure, showing leverage, AUM, and Net Worth.
    """
    print("--- Generating Asset Class Exposure Plot ---")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(script_dir, "PlotsSaved")
    os.makedirs(save_dir, exist_ok=True)
    full_output_path = os.path.join(save_dir, output_filename)

    # --- 1. Data Aggregation (Simplified using Portfolio methods) ---
    exposure_breakdown = portfolio.get_exposure_by_asset_class('EUR')
    value_breakdown = portfolio.get_value_by_asset_class('EUR')
    
    plot_data = []
    for ac in exposure_breakdown:
        if exposure_breakdown[ac] != 0:
            unleveraged_val = value_breakdown.get(ac, Decimal('0'))
            # For Debits, unleveraged and leveraged values are the same
            if ac == 'debit':
                unleveraged_val = exposure_breakdown[ac]
            plot_data.append([ac.capitalize(), unleveraged_val, exposure_breakdown[ac]])

    df = pd.DataFrame(plot_data, columns=['Asset Class', 'Unleveraged Value', 'Leveraged Value'])
    df['Leverage Portion'] = df['Leveraged Value'] - df['Unleveraged Value']

    # --- 2. Add AUM and Net Worth Totals ---
    aum = portfolio.total_aum('EUR').amount
    net_worth = portfolio.total_value('EUR').amount
    
    aum_row = pd.DataFrame([['AUM', aum, aum, 0]], columns=df.columns)
    net_worth_row = pd.DataFrame([['Net Worth', net_worth, net_worth, 0]], columns=df.columns)
    
    df = pd.concat([df, aum_row, net_worth_row], ignore_index=True)
    df = df.sort_values(by='Leveraged Value', ascending=False)
    
    total_positive_exposure = aum
    
    # --- 3. Print Key Values ---
    print("\nExposure Summary:")
    print(f"Total Leveraged Exposure (AUM): €{total_positive_exposure:,.2f}")
    print(f"Unleveraged Net Worth: €{net_worth:,.2f}")
    
    # --- 4. Plotting ---
    df_plot = df.astype({'Unleveraged Value': float, 'Leverage Portion': float})
    total_positive_exposure_float = float(total_positive_exposure)
    
    sns.set_style("whitegrid")
    plt.rc('font', family='sans-serif')
    fig, ax1 = plt.subplots(figsize=(12, 8))

    for index, row in df_plot.iterrows():
        asset_class = row['Asset Class']
        unleveraged_val = row['Unleveraged Value']
        leverage_val = row['Leverage Portion']
        total_val = unleveraged_val + leverage_val

        # Define colors and transparency
        base_color = '#b20710' if total_val < 0 else '#444444' # Dark grey for assets, red for debits
        alpha = 1.0
        if asset_class == 'Net Worth':
            base_color = '#AAAAAA'  # Light grey
            alpha = 0.7
        if asset_class == 'AUM':
            base_color = '#777777'  # Medium grey
            alpha = 0.8
        
        # Draw the bars
        ax1.bar(asset_class, unleveraged_val, color=base_color, alpha=alpha)
        if leverage_val > 0:
            ax1.bar(asset_class, leverage_val, bottom=unleveraged_val, color='#E32227') # Bright red for leverage
            ax1.text(asset_class, unleveraged_val + leverage_val / 2, f'€{leverage_val:,.0f}', ha='center', va='center', color='white', weight='bold', fontsize=9)

        # Add total value label
        offset = total_positive_exposure_float * 0.015 if total_val > 0 else -total_positive_exposure_float * 0.04
        ax1.text(asset_class, total_val + offset, f'€{total_val:,.0f}', ha='center', fontsize=10, weight='bold')

    # --- 5. Dual Y-Axis and Styling ---
    ax2 = ax1.twinx()
    min_val, max_val = ax1.get_ylim()
    ax2.set_ylim(min_val / total_positive_exposure_float * 100, max_val / total_positive_exposure_float * 100)
    ax2.yaxis.set_major_formatter(mticker.PercentFormatter())

    fig.suptitle('Portfolio Exposure by Asset Class', fontsize=16, weight='bold')
    ax1.set_title('Market assets are stacked to show leveraged vs. unleveraged value', fontsize=10, style='italic')
    ax1.set_xlabel('Asset Class', fontsize=12)
    ax1.set_ylabel('Value (€)', fontsize=12, color='#444444')
    ax2.set_ylabel('Percentage of Total Exposure (AUM)', fontsize=12, color='#444444')
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
        plot_asset_class_exposure(portfolio)
    except ImportError:
        print("Could not import portfolio from Constants/ActualConstants.py")