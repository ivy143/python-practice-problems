# Sentiment analysis in tweets
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
# Function to fetch tweets and analyze sentiment
def analyze_tweet_sentiments(username, tweet_count=100):
    tweets = api.user_timeline(screen_name=username, count=tweet_count, tweet_mode='extended')
    tweet_data = []
    for tweet in tweets:
        analysis = TextBlob(tweet.full_text)
        sentiment = 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'
        tweet_data.append({'tweet': tweet.full_text, 'sentiment': sentiment})
    return pd.DataFrame(tweet_data)
# Example usage
username = 'twitter_username'  # Replace with the target Twitter username
tweet_count = 100  # Number of tweets to analyze
df = analyze_tweet_sentiments(username, tweet_count)

# Plotting the sentiment distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='sentiment', order=['positive', 'neutral', 'negative'])
plt.title(f"Sentiment Analysis of @{username}'s Last {tweet_count} Tweets")
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.show()
# Display the first few analyzed tweets
print(df.head())
# Note: To run this code, you need to have valid Twitter API credentials and the required libraries installed.
# You can install the required libraries using:
# pip install tweepy textblob matplotlib pandas seaborn
# Also, ensure that you comply with Twitter's API usage policies.
