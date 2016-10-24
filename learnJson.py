import json


with open('tweets.txt') as f:
data = {}
q = 'asdf'
w = 'ewrt'
e = 'oih'
x=0
for x in range(0, 10):
	data['key']= q+w+e
	json_data = json.dumps(data)

print(json_data)