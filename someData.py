import tweepy
import json
from tweepy import OAuthHandler
 
consumer_key = 'T0it6wF6VyA7nXxdpDIGNAB0z'
consumer_secret = 'ALsd1wd7VXnCOlgfaIchd9LkUC7CQeeuB0JxcrdwNkrjrh1fT9'
access_token = '360929924-dUZHb1IGudb8bvgvjNW2sdjnqWg1QGo2hiwmC2wI'
access_secret = 'pmbN8bKm4mM3JA6pRjGmnKLNRqyB92gCpA7PBKORjHr8q'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

names = []

def process_or_store(tweet):
    print(json.dumps(tweet))

def print_mentions_name(tweet):
	for each in tweet["user_mentions"]:
		print (each["screen_name"])
 

def print_geo(tweet):
	print(tweet["geo"])

def print_friend_screen_name(tweet):
	names.append(tweet["screen_name"])


for tweet in tweepy.Cursor(api.user_timeline, id="DoorThatPivots2").items(1):
	#print_mentions_name(tweet.entities)
	#print_geo(tweet._json)
	print(tweet._json)


#for friend in tweepy.Cursor(api.friends, id="fanchazstic").items(10):
    #print_friend_screen_name(friend._json)
   # #example json respon in friend_json.txt
