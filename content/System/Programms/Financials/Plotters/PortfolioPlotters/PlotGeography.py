#!/usr/bin/env python3
"""
Plots the portfolio's geographical exposure based on leveraged market asset values.
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

def plot_geographical_exposure(portfolio: Portfolio, output_filename: str = "geographical_exposure.png"):
    """
    Generates and saves a bar chart of the portfolio's geographical exposure.

    This analysis considers ONLY LiquidAssets (stocks, ETFs) and uses their
    LEVERAGED value, stacking the bars to show the leveraged portion in red.
    """
    print("--- Generating Geographical Exposure Plot (Leveraged) ---")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(script_dir, "PlotsSaved")
    os.makedirs(save_dir, exist_ok=True)
    full_output_path = os.path.join(save_dir, output_filename)

    # --- 1. Data Aggregation (Enhanced for Leverage) ---
    geo_data = {}
    converter = portfolio._converter

    for asset in portfolio.assets:
        if isinstance(asset, LiquidAssets):
            geography = getattr(asset, 'geography', 'Else')
            if geography not in geo_data:
                geo_data[geography] = {'unleveraged': Decimal('0'), 'leveraged': Decimal('0')}
            
            unleveraged_val = getattr(asset, 'actual_current_value', None)
            leveraged_val = getattr(asset, 'current_value', None)
            
            if unleveraged_val and leveraged_val:
                geo_data[geography]['unleveraged'] += converter.convert(unleveraged_val, 'EUR').amount
                geo_data[geography]['leveraged'] += converter.convert(leveraged_val, 'EUR').amount

    # --- 2. Data Preparation ---
    if not geo_data:
        print("No market assets with geographical data found. Skipping plot.")
        return

    plot_data = []
    for geo, values in geo_data.items():
        plot_data.append([geo, values['unleveraged'], values['leveraged']])

    df = pd.DataFrame(plot_data, columns=['Geography', 'Unleveraged Value', 'Leveraged Value'])
    df['Leverage Portion'] = df['Leveraged Value'] - df['Unleveraged Value']
    
    total_leveraged_exposure = df['Leveraged Value'].sum()
    if total_leveraged_exposure == 0:
        print("Total market value is zero. Skipping plot generation.")
        return

    df['Percentage'] = df['Leveraged Value'].apply(lambda x: (x / total_leveraged_exposure) * 100)
    df = df.sort_values(by='Leveraged Value', ascending=False)

    # --- 3. Print Key Values ---
    print("\nGeographical Exposure Summary (Leveraged):")
    print(f"Total Market Exposure: €{total_leveraged_exposure:,.2f}")
    print("-" * 55)
    print(f"{'Geography':<20} | {'Leveraged Value (€)':>20} | {'Percentage':>12}")
    print("-" * 55)
    for index, row in df.iterrows():
        print(f"{row['Geography']:<20} | {row['Leveraged Value']:>20,.2f} | {row['Percentage']:>11.2f}%")
    print("-" * 55)

    # --- 4. Plotting ---
    df_plot = df.astype({'Unleveraged Value': float, 'Leverage Portion': float})
    total_exposure_float = float(total_leveraged_exposure)
    
    sns.set_style("whitegrid")
    plt.rc('font', family='sans-serif')
    fig, ax1 = plt.subplots(figsize=(10, 7))

    # Draw the bars manually for stacking control
    ax1.bar(df_plot['Geography'], df_plot['Unleveraged Value'], color='#444444')
    ax1.bar(df_plot['Geography'], df_plot['Leverage Portion'], bottom=df_plot['Unleveraged Value'], color='#b20710')

    # Add labels
    for index, row in df_plot.iterrows():
        leverage_val = row['Leverage Portion']
        total_val = row['Unleveraged Value'] + leverage_val
        
        # Add total value label
        offset = total_exposure_float * 0.015
        ax1.text(row['Geography'], total_val + offset, f'€{total_val:,.0f}', ha='center', fontsize=10, weight='bold')

        # Add label inside the red leverage portion, if it exists
        if leverage_val > 5: # Threshold to avoid tiny labels
            ax1.text(row['Geography'], row['Unleveraged Value'] + leverage_val / 2,
                     f'€{leverage_val:,.0f}', ha='center', va='center', color='white', weight='bold', fontsize=9)

    # --- 5. Dual Y-Axis and Styling ---
    ax2 = ax1.twinx()
    min_val, max_val = ax1.get_ylim()
    ax2.set_ylim(min_val / total_exposure_float * 100, max_val / total_exposure_float * 100)
    ax2.yaxis.set_major_formatter(mticker.PercentFormatter())

    fig.suptitle('Geographical Exposure of Market Assets', fontsize=16, weight='bold')
    ax1.set_title('Based on leveraged asset values', fontsize=10, style='italic')
    ax1.set_xlabel('Geography', fontsize=12)
    ax1.set_ylabel('Leveraged Value (€)', fontsize=12, color='#444444')
    ax2.set_ylabel('Percentage of Market Assets', fontsize=12, color='#444444')
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
        plot_geographical_exposure(portfolio)
    except ImportError:
        print("Could not import portfolio from Constants/ActualConstants.py")
        print("Please run this plotter via main.py")