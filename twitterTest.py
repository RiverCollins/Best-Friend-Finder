
import tweepy
import csv

#Twitter API Creds
consumer_token = "T0it6wF6VyA7nXxdpDIGNAB0z"
consumer_secret = "ALsd1wd7VXnCOlgfaIchd9LkUC7CQeeuB0JxcrdwNkrjrh1fT9"
access_token = "360929924-dUZHb1IGudb8bvgvjNW2sdjnqWg1QGo2hiwmC2wI"
access_secret = "pmbN8bKm4mM3JA6pRjGmnKLNRqyB92gCpA7PBKORjHr8q"


#Authorize Twitter
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user = api.get_user('fanchazstic ')





