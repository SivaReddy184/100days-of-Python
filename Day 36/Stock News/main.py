import requests
from twilio.rest import Client

account_sid = "ACbf8956a7302c341b"
auth_token = "abc"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "abc"
NEWS_API_KEY = "6abc96"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}"
                        f"&apikey={API_KEY}")
data = response.json()
days_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in days_data.items()]

yesterday_closed = float(data_list[0]["4. close"])
day_before_yesterday_closed = float(data_list[1]["4. close"])

difference = yesterday_closed - day_before_yesterday_closed
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round(difference / yesterday_closed * 100)

if abs(diff_percent) > 5:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news = requests.get(f"https://newsapi.org/v2/everything?q={STOCK}&qInTitle={COMPANY_NAME}&apiKey={NEWS_API_KEY}")
    data = news.json()
    latest_articles = data["articles"]
    three_articles = latest_articles[:2]

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=article,
            from_="+19259404526",
            to="+9116122022"
        )
        print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
