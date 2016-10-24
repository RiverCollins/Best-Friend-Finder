#Gets 10 tweets from user fanchazstic
#Saves each tweet into one big file
import tweepy
import json
import simplejson

#Twitter API Creds
consumer_token = "T0it6wF6VyA7nXxdpDIGNAB0z"
consumer_secret = "ALsd1wd7VXnCOlgfaIchd9LkUC7CQeeuB0JxcrdwNkrjrh1fT9"
access_token = "360929924-dUZHb1IGudb8bvgvjNW2sdjnqWg1QGo2hiwmC2wI"
access_secret = "pmbN8bKm4mM3JA6pRjGmnKLNRqyB92gCpA7PBKORjHr8q"


#Authorize Twitter
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


#puts json data from tweet into json file
def make_json_file(number, tweet):
	file_name = ('Test\BigData.json')
	file = open(file_name, 'a')
	file.close()
	process_or_store(tweet, file_name)



def process_or_store(tweet, file_name):
	#print(json.dumps(tweet))
	print(asdf)
	jsondata = simplejson.dumps(tweet, indent=4, skipkeys=True, sort_keys=True)
	fd = open(file_name, 'a')
	fd.write(jsondata)
	fd.close()

asdf = 0

#Gets user id
user = api.get_user(screen_name = 'fanchazstic')


for tweet in tweepy.Cursor(api.user_timeline, id=user.id).items(10):
    make_json_file(asdf, tweet._json)
    asdf = asdf + 1

    
