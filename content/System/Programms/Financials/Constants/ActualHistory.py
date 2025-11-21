#!/usr/bin/env python3
"""
ActualHistory.py
Creates a timeline object based on the current, real portfolio.
"""
import sys
import os

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Imports ---
from FinancialClasses.PortfolioInTime import PortfolioInTime
from Constants.ActualConstants import portfolio as actual_portfolio

# --- Timeline Definition ---
# This is the timeline for your actual portfolio, with no future modifications.
timeline = PortfolioInTime(actual_portfolio)