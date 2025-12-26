def generate_explanation(stock_data: dict):
    reasons = [ ]
    summary = ""

    change = stock_data["percent_change"]
    volume = stock_data["volume"]

    # Price movement logic
    if change > 1:
        reasons.append("Stock showed strong upward movement today")
    elif change > 0:
        reasons.append("Stock moved slightly upward today")
    elif change < -1:
        reasons.append("Stock declined significantly today")
    else:
        reasons.append("Stock showed minor decline today")

    # Volume logic
    if volume > 5_000_000:
        reasons.append("High trading volume indicates strong market activity")
    else:
        reasons.append("Moderate trading volume observed")

    # Summary generation
    if change > 0:
        summary = "The stock moved up today due to buying interest from the market."
    else:
        summary = "The stock moved down today due to selling pressure in the market."

    return {
        "summary": summary,
        "reasons": reasons
    }
