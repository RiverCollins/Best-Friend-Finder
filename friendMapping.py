import tweepy
import json
import sys
import csv
import time
import simplejson
import os
from tweepy import OAuthHandler
 
consumer_key = 'T0it6wF6VyA7nXxdpDIGNAB0z'
consumer_secret = 'ALsd1wd7VXnCOlgfaIchd9LkUC7CQeeuB0JxcrdwNkrjrh1fT9'
access_token = '360929924-dUZHb1IGudb8bvgvjNW2sdjnqWg1QGo2hiwmC2wI'
access_secret = 'pmbN8bKm4mM3JA6pRjGmnKLNRqyB92gCpA7PBKORjHr8q'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


def top_friends(name, num_fri):
	friends = []
	with open(name + 'Sorted.csv' , 'r') as fh:
		reader = csv.reader(fh, delimiter = ',')
		i = 0
		for row in reader:
			if(i >= num_fri):
				break;
			friends.append(row[0])
			i = i + 1
	return friends

#opens file created by write_to_file_freq_of_mentions function and sorts them. returns the sorted list
def sort_list(name):
	with open(name + '.csv','r') as fh:
  		reader = csv.reader(fh, delimiter = ',')
  		sort = sorted(reader, key=lambda x: int(x[1]), reverse=True)
	return sort

#opens file created by write_to_file_freq_of_mentions and get the nubmer of rows. Needed to for write_to_file_sorted funciton
def get_row_number(name):
	with open(name + '.csv','r') as fh:
		reader = csv.reader(fh, delimiter = ',')
		row_count = sum(1 for row in reader)
	return row_count

#finds the reeq of each name in the mentions list
def freq(asdf):
	wordfreq = [asdf.count(p) for p in asdf]
	return wordfreq

def friends(tweet):
	names = []
	names.append(tweet["user_name"])
	return names

#in each tweet looks for the uer_mentions type in the tweet and add each screen_name to the names list
def mentions_name(tweet):
	for each in tweet["user_mentions"]:
		mentions.append(each["user_name"])
		print(each["screen_name"])

def get_friends(x, name):
	for friend in tweepy.Cursor(api.friends, id=name).items(x):
		friends(friend._json)

def make_json_file(number, tweet, cwd):
	file_name = (cwd + '\\' + str(number) +'.json')
	file = open(file_name, 'w')
	file.close()
	process_or_store(tweet, file_name)

def process_or_store(tweet, file_name):
	#print(json.dumps(tweet))
	jsondata = simplejson.dumps(tweet, indent=4, skipkeys=True, sort_keys=True)
	fd = open(file_name, 'w')
	fd.write(jsondata)
	fd.close()

#sends each tweet to the mentions_name function in json format
def get_mentions(x, name, cwd):
	mentions = []
	i = 0
	#saveToDir = cwd + '\\' + name
	#print(saveToDir)
	if(os.path.exists(cwd)!= True):
		os.mkdir(cwd)
	for tweet in tweepy.Cursor(api.user_timeline, id = name).items(x):
		#mentions_name(tweet.entities)
		fullTweet = (tweet._json)
		make_json_file(i, fullTweet, cwd)
		tweet = tweet.entities
		for each in tweet["user_mentions"]:
			mentions.append(each["screen_name"])
		#time.sleep(5)#-----------------------------------------------------------------------------
		print(str(i) + ' Got Tweet!')
		i = i + 1
	return mentions


def write_to_file_sorted(name):
	row_count = get_row_number(name)
	sort = sort_list(name)

	f = open(name + 'Sorted.csv' , 'w', newline = '')
	try:
		writer = csv.writer(f)
		i = 0
		for i in range(row_count):
			writer.writerow(sort[i])
	finally:
		f.close()

#writes the screen_name and the freq of each name in a csv file
def write_to_file_freq_of_mentions(name, mentions, cwd):
	men_freq = []
	men_freq = freq(mentions)
	used = []
	#os.mkdir(name)
	os.chdir(cwd)
	f = open(name + '.csv' , 'w', newline = '')
	try:
		writer = csv.writer(f)
		#i = 2
		y = 0
		for i in range(len(mentions)):
			key = mentions[i]
			if key in used:
				skip = 1
			else:	
				writer.writerow((mentions[i], men_freq[i]))
				used.append(mentions[i])
	finally:
		f.close()

def get_info_of_mentons(user_name, number_of_tweets, cwd):
	newCwd = cwd + '\\' + user_name
	if(os.getcwd() != newCwd):
		os.mkdir(newCwd)
		os.chdir(newCwd)

	mentions = []

	mentions = get_mentions(number_of_tweets, user_name, newCwd)
	print('Got Mentions')
	write_to_file_freq_of_mentions(user_name, mentions, cwd)
	print('Created Unsorted File')
	write_to_file_sorted(user_name)
	print('-------------------')

#python friendMapping.py TwitterName numberOfTweetsToGoThrou
def main(argv):
	number_of_tweets = int(sys.argv[2])
	user_name = sys.argv[1]
	cwd = os.getcwd() + '\\' + user_name

	mentions = []
	best_friends = []

	mentions = get_mentions(number_of_tweets, user_name, cwd)
	print('Got Mentions')
	write_to_file_freq_of_mentions(user_name, mentions, cwd)
	print('Created Unsorted File')
	write_to_file_sorted(user_name)
	best_friends = top_friends(user_name, 10)
	print('-------------------')

	for i in range(10):
		get_info_of_mentons(best_friends[i], number_of_tweets, cwd)



if __name__ == "__main__":
	main(sys.argv[1:])


	#getting each acctount to have there own folder