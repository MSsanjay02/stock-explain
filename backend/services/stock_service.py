import yfinance as yf

def get_stock_data(symbol: str):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="5d")

        # If no data returned
        if data is None or data.empty or len(data) < 2:
            return None

        latest = data.iloc[-1]
        previous = data.iloc[-2]

        return {
            "symbol": symbol,
            "current_price": round(float(latest["Close"]), 2),
            "previous_close": round(float(previous["Close"]), 2),
            "change": round(float(latest["Close"] - previous["Close"]), 2),
            "percent_change": round(
                ((latest["Close"] - previous["Close"]) / previous["Close"]) * 100, 2
            ),
            "volume": int(latest["Volume"])
        }

    except Exception as e:
        print("Stock service error:", e)
        return None
