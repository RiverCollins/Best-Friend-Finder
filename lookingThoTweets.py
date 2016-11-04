import os
import sys
import json

def json_data(cwd, name):
	print('----------------------')
	for root, dir, files in os.walk(dir):
		for file in files:
			if file.endswith(".json"):
				with open(file) as data_file:
					data = json.load(data_file)
					#print(data["user"]["screen_name"])

def main(argv):
	user_name = sys.argv[1]
	os.chdir(os.getcwd() + '\\' + user_name)
	cwd = os.getcwd()
	dirs = os.listdir()
	#print(dirs)
	#print(len(dirs))
	for dir in dirs:
		if(os.path.isdir(dir)):
			json_data(cwd, dir)

if __name__ == "__main__":
	main(sys.argv[1:])
