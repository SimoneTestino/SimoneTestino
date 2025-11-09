#!/usr/bin/env python3
"""
main.py
The main entry point for running portfolio analysis and generating plots.
Features a menu to select between analyzing the actual portfolio or future scenarios.
"""

import sys
import os
from datetime import date
import importlib

# --- Path Setup ---
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Import Plotters ---
from Plotters.PortfolioPlotters.PlotAssetsClass import plot_asset_class_exposure
from Plotters.PortfolioPlotters.PlotGeography import plot_geographical_exposure
from Plotters.PortfolioPlotters.PlotCurrency import plot_currency_exposure
from Plotters.PortfolioInTimePlotters.PlotAssetClassInTime import plot_aum_over_time

def find_scenario_files() -> list:
    """Scans the Constants directory for scenario files."""
    constants_dir = os.path.join(project_root, 'Constants')
    files = [f for f in os.listdir(constants_dir) if f.endswith('.py') and 'Scenario' in f]
    return [os.path.splitext(f)[0] for f in files]

def run_plot_selection(timeline):
    """Displays the menu of available plots for a given timeline."""
    print(f"\nUpdating valuation date to: {date.today()} and fetching market data...")
    timeline.initial_portfolio.valuation_date = date.today()
    timeline.start_date = date.today()
    timeline.initial_portfolio.update_all_market_values()
    print("Update complete.")

    plot_menu = {
        '1': ('Asset Class Exposure', plot_asset_class_exposure),
        '2': ('Geographical Exposure', plot_geographical_exposure),
        '3': ('Currency Exposure', plot_currency_exposure),
        '4': ('Portfolio Value Over Time', plot_aum_over_time),
    }

    while True:
        print("\n" + "="*50)
        print("          Select a Plot")
        print("="*50)
        for key, (name, _) in plot_menu.items():
            print(f"  {key}. {name}")
        print("\n  B. Back to Main Menu")
        print("-" * 50)
        
        choice = input("Enter your choice: ").strip().lower()

        if choice in plot_menu:
            plot_name, plot_function = plot_menu[choice]
            print(f"\n--- Generating '{plot_name}' Plot ---")
            try:
                if plot_function in [plot_aum_over_time]:
                    # This plot requires time arguments
                    plot_function(timeline, years_past=1, years_future=15)
                else:
                    plot_function(timeline.initial_portfolio)
            except Exception as e:
                print(f"\nAn error occurred while generating the plot: {e}")
        elif choice == 'b':
            break
        else:
            print("\nInvalid choice.")

def handle_scenario_analysis():
    """Handles the menu for selecting and analyzing a future scenario."""
    scenarios = find_scenario_files()
    if not scenarios:
        print("\nNo scenario files found in the 'Constants' directory.")
        return

    while True:
        print("\n" + "="*50)
        print("        Select a Scenario to Analyze")
        print("="*50)
        for i, name in enumerate(scenarios, 1):
            print(f"  {i}. {name}")
        print("\n  B. Back to Main Menu")
        print("-" * 50)

        choice = input("Enter your choice: ").strip().lower()
        if choice == 'b':
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(scenarios):
                scenario_name = scenarios[index]
                print(f"\nLoading scenario '{scenario_name}'...")
                # Dynamically import the chosen scenario module
                scenario_module = importlib.import_module(f"Constants.{scenario_name}")
                run_plot_selection(scenario_module.timeline)
            else:
                print("\nInvalid number.")
        except (ValueError, ImportError) as e:
            print(f"\nCould not load scenario: {e}")

def main_menu():
    """Displays the top-level menu."""
    while True:
        print("\n" + "="*50)
        print("          MAIN MENU")
        print("="*50)
        print("  1. Analyze Actual Portfolio (from ActualConstants)")
        print("  2. Analyze a Future Scenario")
        print("\n  Q. Quit")
        print("-" * 50)
        
        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            try:
                from Constants.ActualHistory import timeline
                run_plot_selection(timeline)
            except ImportError:
                print("\nError: Could not find 'ActualHistory.py'. Please ensure it exists in 'Constants/'.")
        elif choice == '2':
            handle_scenario_analysis()
        elif choice == 'q':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or Q.")

if __name__ == "__main__":
    main_menu()