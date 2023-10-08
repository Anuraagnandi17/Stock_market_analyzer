import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import yfinance as yf
from textblob import TextBlob  # Import TextBlob for sentiment analysis

# Define your News API endpoint and API key
news_api_endpoint = "https://newsapi.org/v2/everything"
api_key = "c4b93e9d513b455585cacba8455edaf3"

# Define the stock symbol for which you want news (e.g., MICROSOFT)
stock_symbol = "MICROSOFT"

# Define the number of days for which you want to retrieve news
days_ago = 1  # Change this to the desired number of days

# Calculate the start and end dates for the date range
end_date = datetime.now()
start_date = end_date - timedelta(days=days_ago)

# Format the dates in the required format (e.g., YYYY-MM-DD)
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

# Define the query parameters
query_params = {
    "q": f"{stock_symbol} stock",
    "from": start_date_str,
    "to": end_date_str,
    "apiKey": api_key,
}

# Make a request to the News API
response = requests.get(news_api_endpoint, params=query_params)

# Check if the request was successful
if response.status_code == 200:
    news_data = response.json()
    articles = news_data.get("articles", [])

    # Create lists to store the titles and sentiments
    titles = []
    sentiments = []

    # Iterate through news articles and perform sentiment analysis
    for article in articles:
        title = article.get("title", "")
        if stock_symbol.lower() in title.lower():
            print(f"Title: {title}")

            # Perform sentiment analysis using TextBlob
            analysis = TextBlob(title)
            sentiment = analysis.sentiment.polarity

            # Determine sentiment (positive, negative, neutral)
            if sentiment > 0:
                sentiment_label = "Positive"
            elif sentiment < 0:
                sentiment_label = "Negative"
            else:
                sentiment_label = "Neutral"

            print(f"Sentiment: {sentiment_label}\n")

            # Store the title and sentiment
            titles.append(title)
            sentiments.append(sentiment_label)

else:
    print("Failed to fetch news. Status code:", response.status_code)

# Define the stock symbol (e.g., RELIANCE.BO)
stock_symbol = "RELIANCE.BO"

# Fetch historical stock data using Yahoo Finance API
stock_data = yf.download(stock_symbol, period="1d", interval="1d")

# Print the stock data
print(stock_data.head())
