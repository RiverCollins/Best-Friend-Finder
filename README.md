# Best Friend Finder
I made these two scripts to scan a user's tweets and create a list of people the user mentions. I used this list to make graph displaying how this user is connected to other users.

You will need these two libaries to run the script:

Tweepy http://www.tweepy.org/

NetworkX https://networkx.github.io/

# Map Twitter Account
This script looks at a user's tweets, puts every mention into a CSV file, and orders them from most mentioned to least mentioned. The script then identifies the ten most mentioned users, looks at their tweets, and creates a CSV file for those ten.
The script takes two command line arguments: user and num, where user is the twitter handle and num is the number of tweets to look at.

Example:

         python MapTwitterAccount.py DoorThatPivots2 100
         
This would map my twitter account and look at 100 tweets.

#Display Nodes
This script takes the CSV files and displays them. Each user account is a node. The top five users in each CSV file get displayed with lines connecting them.

Example:

         python DisplayNodes DoorThatPivots2
         
Here is an example of what a graph wolgl look like. I used Target's twitter as my base.
![capture](https://cloud.githubusercontent.com/assets/22608326/23097059/2139a5c2-f5f0-11e6-9f3b-f2ef55c583bf.PNG)
         
         
#Helpful Tips
The scripts try to make sure that twitter does not limit you, but still read up on rate limits
https://dev.twitter.com/rest/public/rate-limiting

Keep both scrpts in the same directory as they use it to save the CSV files and tweets along with reading them.
