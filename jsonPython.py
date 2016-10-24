#http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
import json

def write_tweets(text):
	file = open('tweets.txt', 'a')
	file.write(text)
	file.close()

x = 0
for x in range(0, 10):
	file_name = ('ChazTweets\data' + str(x) +'.json')
#opens josn file and load it into data
	with open(file_name) as data_file:
		data = json.load(data_file)
		asdf = data['text']
		write_tweets(asdf)
		print(x)

