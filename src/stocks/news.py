import requests
from config import news_key

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def get_news(query):
    """Return first 3 articles with the query in the title"""
    news_params = {
        # 'q':STOCK_NAME,
        "qintitle": query,
        "apikey": news_key
    }
    return requests.get(NEWS_ENDPOINT, params=news_params).json()["articles"][:3]