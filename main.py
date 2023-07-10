import tweepy
import time

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Hashtag to search for
hashtag = "your_hashtag"

# Number of tweets to like
num_likes = 10

# Function to like tweets with a given hashtag
def like_tweets_with_hashtag():
    tweets = tweepy.Cursor(api.search, hashtag).items(num_likes)
    for tweet in tweets:
        try:
            tweet.favorite()
            print("Liked a tweet: ", tweet.text)
        except tweepy.TweepError as e:
            print("Error liking tweet: ", e.reason)
        except StopIteration:
            break

# Main bot loop
while True:
    like_tweets_with_hashtag()
    time.sleep(60)  # Sleep for 1 minute before liking more tweets