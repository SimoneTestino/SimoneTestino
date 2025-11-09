#!/usr/bin/env python3
"""
Plots the portfolio's historical and forecasted composition over time as a stacked area chart.
"""

import sys
import os

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
plotters_dir_parent = os.path.dirname(current_dir)
project_root = os.path.dirname(plotters_dir_parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Imports ---
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from dateutil.relativedelta import relativedelta

from FinancialClasses.PortfolioInTime import PortfolioInTime

def plot_aum_over_time(
    timeline: PortfolioInTime,
    years_past: int,
    years_future: int,
    output_filename: str = "aum_over_time.png"
):
    """
    Generates a stacked area chart of the portfolio's value and composition over time.
    """
    print("--- Generating AUM Over Time Plot ---")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(script_dir, "PlotsSaved")
    os.makedirs(save_dir, exist_ok=True)
    full_output_path = os.path.join(save_dir, output_filename)

    # 1. Generate Time Series Data
    today = timeline.start_date
    start_date = today - relativedelta(years=years_past)
    end_date = today + relativedelta(years=years_future)
    
    date_range = pd.date_range(start=start_date, end=end_date, freq='QE').to_pydatetime()
    
    print("Calculating portfolio composition at each point in time... (this may take a moment)")
    plot_data = []
    for snapshot_datetime in date_range:
        snapshot_date = snapshot_datetime.date()
        p_snapshot = timeline.get_portfolio_at_date(snapshot_date, scenario_name='constant_growth')
        if snapshot_date <= today:
            p_snapshot.update_all_market_values()
        
        class_values = p_snapshot.get_value_by_asset_class('EUR')
        aum = class_values['market'] + class_values['liquidity'] + class_values['illiquid'] + class_values['credit']
        net_worth = aum + class_values['debit']
        plot_data.append({'Date': snapshot_date, **class_values, 'AUM': aum, 'Net Worth': net_worth})

    df = pd.DataFrame(plot_data)
    numeric_cols = [col for col in df.columns if col != 'Date']
    df[numeric_cols] = df[numeric_cols].astype(float)
    
    # 2. Print Key Values
    initial_p = timeline.get_portfolio_at_date(today)
    initial_p.update_all_market_values()
    initial_value = float(initial_p.total_value('EUR').amount)
    final_value = float(df['Net Worth'].iloc[-1]) if not df.empty else 0.0
    
    print("\nForecast Summary:")
    print(f"  Initial Value ({today}): €{initial_value:,.2f}")
    print(f"  Forecasted Value ({end_date}): €{final_value:,.2f}")

    # 3. Plotting
    plt.style.use('grayscale')
    fig, ax = plt.subplots(figsize=(15, 9))
    
    asset_classes = ['market', 'liquidity', 'illiquid', 'credit']
    colors = ['#333333', '#666666', '#999999', '#CCCCCC']
    labels = [c.capitalize() for c in asset_classes]

    ax.stackplot(df['Date'], df[asset_classes].T, labels=labels, colors=colors, alpha=0.8)
    ax.fill_between(df['Date'], df['debit'], 0, color='#b20710', alpha=0.7, label='Debit')
    ax.plot(df['Date'], df['AUM'], color='black', linewidth=2.5, label='Assets Under Management (AUM)')
    ax.plot(df['Date'], df['Net Worth'], color='#b20710', linewidth=3, label='Net Worth')

    # --- EDIT: Changed color from 'red' to 'black' ---
    ax.axvline(x=today, color='black', linestyle='--', linewidth=1.5, label='Present')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.7)

    # 4. Styling and Labels
    ax.set_title('Portfolio Composition and Net Worth Over Time', fontsize=18, weight='bold')
    ax.set_ylabel('Value (€)', fontsize=12)
    ax.get_yaxis().set_major_formatter(mticker.FuncFormatter(lambda x, p: f'€{int(x):,}'))
    ax.legend(loc='upper left')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    fig.tight_layout()
    
    # 5. Save and Show
    plt.savefig(full_output_path, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved successfully as '{full_output_path}'")
    plt.show()

# --- Example Usage ---
if __name__ == '__main__':
    try:
        from Constants.HyperDebitScenarioAug25 import timeline
        plot_aum_over_time(timeline, years_past=1, years_future=15)
    except ImportError as e:
        print(f"Could not import a timeline from a scenario file: {e}")