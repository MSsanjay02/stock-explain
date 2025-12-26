import yfinance as yf
from datetime import datetime

def get_stock_data(symbol: str):
    try:
        ticker = yf.Ticker(symbol)

        # Fetch recent data (safe for weekends & holidays)
        hist = ticker.history(period="5d", interval="1d")

        if hist is None or hist.empty or len(hist) < 2:
            return None

        latest = hist.iloc[-1]
        previous = hist.iloc[-2]

        return {
            "symbol": symbol,
            "current_price": round(float(latest["Close"]), 2),
            "previous_close": round(float(previous["Close"]), 2),
            "change": round(float(latest["Close"] - previous["Close"]), 2),
            "percent_change": round(
                ((latest["Close"] - previous["Close"]) / previous["Close"]) * 100, 2
            ),
            "volume": int(latest["Volume"]),
            "source": "Yahoo Finance",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        print("Yahoo Finance error:", e)
        return None
