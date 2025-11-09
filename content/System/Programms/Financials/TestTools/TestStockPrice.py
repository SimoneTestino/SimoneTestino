#!/usr/bin/env python3
"""
Stock Price Tester
Simple program to test stock price fetching functionality.
"""

import sys
import os
from datetime import date
from decimal import Decimal

# Add parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import the stock price functions
from Helper.FetchStockPrice import (
    fetch_close_price,
    find_previous_close,
    guess_currency_from_ticker,
    StockValuationHelper
)

def test_ticker(ticker: str):
    """Test fetching price for a given ticker."""
    print(f"\n{'='*60}")
    print(f"TESTING TICKER: {ticker.upper()}")
    print(f"{'='*60}")
    
    # 1. Basic info
    currency = guess_currency_from_ticker(ticker)
    print(f"Guessed Currency: {currency}")
    
    # 2. Test StockValuationHelper
    print(f"\n--- StockValuationHelper Test ---")
    try:
        helper = StockValuationHelper(ticker)
        print(f"Ticker Available: {helper.is_available}")
        print(f"Currency Code: {helper.currency_code}")
        
        # Get current price (with manual fallback)
        print(f"\n--- Fetching Current Price ---")
        current_price = helper.get_current_price()
        if current_price:
            print(f"✓ Current Price: {current_price}")
        else:
            print(f"✗ Failed to get current price")
            
    except Exception as e:
        print(f"✗ StockValuationHelper Error: {e}")
    
    # 3. Test direct functions
    print(f"\n--- Direct Function Tests ---")
    
    # Today's price
    today = date.today()
    print(f"Fetching price for {today}:")
    today_price = fetch_close_price(ticker, today)
    if today_price:
        print(f"✓ Today's Price: {today_price} {currency}")
    else:
        print(f"✗ No price found for today")
    
    # Previous close (30 days back)
    print(f"Searching for previous close (last 30 days):")
    prev_price = find_previous_close(ticker, today, 30)
    if prev_price:
        print(f"✓ Previous Close: {prev_price} {currency}")
    else:
        print(f"✗ No previous price found in last 30 days")

def main():
    """Main testing loop."""
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                    STOCK PRICE TESTER                     ║")
    print("║              Test the fetch stock price tool              ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    while True:
        print(f"\n{'='*60}")
        ticker = input("Enter a ticker symbol (or 'quit' to exit): ").strip()
        
        if ticker.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not ticker:
            print("❌ Please enter a valid ticker symbol.")
            continue
        
        try:
            test_ticker(ticker)
        except KeyboardInterrupt:
            print("\n\n🛑 Test interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error testing {ticker}: {e}")
        
        # Ask if user wants to continue
        print(f"\n{'='*60}")
        continue_test = input("Test another ticker? (y/n): ").strip().lower()
        if continue_test not in ['y', 'yes']:
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()