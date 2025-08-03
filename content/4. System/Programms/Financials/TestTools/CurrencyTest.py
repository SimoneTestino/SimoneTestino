import yfinance as yf

try:
    ticker = yf.Ticker("EURUSD=X")
    
    # Use history() to get the most recent data
    hist = ticker.history(period="1d")
    
    if not hist.empty:
        # Get the last closing price from the returned data
        price = hist['Close'].iloc[-1]
        print(f"✅ Successfully fetched EUR/USD price: {price}")
    else:
        print("❌ Connection made, but history() returned no data.")

except Exception as e:
    print(f"❌ Connection to yfinance failed entirely: {e}")