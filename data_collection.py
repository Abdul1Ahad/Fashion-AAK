import tweepy
import pandas as pd
from textblob import TextBlob

# Initialize Twitter API client
client = tweepy.Client(bearer_token='YOUR_BEARER_TOKEN')
query = "#fashion OR #style OR #fashiontrends lang:en -is:retweet"
tweets = client.search_recent_tweets(query=query, tweet_fields=["created_at", "text", "author_id", "public_metrics"], max_results=100)

# Parse and analyze sentiment
data = []
for tweet in tweets.data:
    polarity = TextBlob(tweet.text).sentiment.polarity
    sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
    data.append([
        tweet.created_at, tweet.author_id, tweet.text,
        tweet.public_metrics['like_count'],
        tweet.public_metrics['retweet_count'],
        sentiment
    ])

# Save to CSV
columns = ['Timestamp', 'Author_ID', 'Tweet', 'Likes', 'Retweets', 'Sentiment']
df = pd.DataFrame(data, columns=columns)
df.to_csv("fashion_sentiment_dataset.csv", index=False)
