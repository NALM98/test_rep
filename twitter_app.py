import tweepy
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

me = api.me()
line = "My name is {}, my screen name is {}, I have {} followers, I follow {} accounts"

"print(line.format(me.name, me.screen_name, me.followers_count, me.friends_count))"

tweet = "A king there sat most dark and fell of all who under heaven dwell"
api.update_status(tweet)

my_last_tweet = api.user_timeline(count = 1) [0]
print(my_last_tweet.id, my_last_tweet.user.screen_name, my_last_tweet.text)
