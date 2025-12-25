from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.stock_service import get_stock_data
from services.news_service import get_stock_news

app = FastAPI(title="StockExplain API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "StockExplain backend is running"}

@app.get("/explain-stock")
def explain_stock(symbol: str, company: str):
    stock_data = get_stock_data(symbol)
    news = [ ]

    if not stock_data:
        return {"error": "Invalid stock symbol"}

    return {
        "stock_data": stock_data,
        "news": news
    }
