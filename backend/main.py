from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.stock_service import get_stock_data

# ✅ app MUST be created before using @app.get
app = FastAPI(title="StockExplain API")

# CORS (needed later for frontend)
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

    if not stock_data:
        return {"error": "Stock data not available"}

    return {
        "stock_data": stock_data,
        "news": [],
        "data_note": "Price data powered by Yahoo Finance (near real-time)"
    }
