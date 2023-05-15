import requests
from config import alpha_key
from news import get_news
from texter import send_sms

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK_NAME,
    "apikey": alpha_key

}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# data_list = [new_item for item in list]
data_list = [v for (k,v) in data.items()]
yesterday_data = data_list[0]
y_closing = yesterday_data["4. close"]
before_data = data_list[1]
b_closing= before_data["4. close"]

diff = float(b_closing) - float(y_closing)
perc = round(diff / float( y_closing)  * 100 , 1)
arrow = '🔺' if perc > 0 else '🔻'

if abs(perc > 2 ):
    # Retrieving first 3 articles
    three_articles =get_news(COMPANY_NAME)
    # messages = [ f"\nHeadline : {article['title']}\nBrief: {article['description']}" for article in three_articles]
    message = f"{STOCK_NAME} {arrow}{perc}"
    for article in three_articles:
        message += f"\nHeadline : {article['title']}\nBrief: {article['description']}"
    print(message)
    send_sms(message)


