import requests
import os

NEWS_API_KEY = "Y7f04996c546c421d9bfde19362f958c1"

def get_stock_news(company_name: str):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={company_name}&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data.get("articles", [])[:5]:
        articles.append({
            "title": article["title"],
            "description": article["description"],
            "source": article["source"]["name"]
        })

    return articles
