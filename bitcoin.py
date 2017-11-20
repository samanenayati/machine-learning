import tweepy
import json
import csv

# Twitter API credentials
consumer_key = "e4SFoZ29obOG5LyOBO9Vt0h0S"
consumer_secret = "w8PZ23mDIWLOPeNi7x1Gh643PDTPQ0xW8gYQ7SdYR20b55qCLt"
access_key = "931411823907229697-d5hlkYdGgnt91KQxMn1gZajpettBDrO"
access_secret = "psEgyiYh7cbCAOJLC55DAIgFJMHVEPU420RClMQE4qnWg"

auth = tweepy.auth.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

trends = api.trends_place(1)

# get data for given keyword "bitcoin"
searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q='bitcoin').items(20000)]
json_object = [json.dumps(json_obj) for json_obj in searched_tweets]
json_strings=[json.loads(json_str) for json_str in json_object]

#conver json result to csv file with two columns "text" and "date"

csvdata=open('csvdata1.csv','wb')
csvwriter=csv.writer(csvdata)

for item in json_strings:
    text=item['text']
    date=item['created_at']
    csvwriter.writerow([[date],[text]])

