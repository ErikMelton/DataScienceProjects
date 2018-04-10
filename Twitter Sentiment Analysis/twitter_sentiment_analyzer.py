import tweepy

from textblob import TextBlob

consumer_key = 'GDujIRtAE3b2pIYvw8fmPLenu'
consumer_secret = '3vyAgoy13XpuUPUAzIDg88Q0tz0n23pO1tJDQPHUxEVkrw4oVP'

access_token = '1538985115-DVMAONqOBfDTxtvuF48EVzqMxA4pajWjLmVliOt'
access_token_secret = 'bSzNkWewtgSwQvbou7Fu8JGQspycspbQgAHZrcMAiJOhl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)