import tweepy
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trends1 = api.trends_place(1)
trends = set([trend['name'] for trend in trends1[0]['trends']])
print trends