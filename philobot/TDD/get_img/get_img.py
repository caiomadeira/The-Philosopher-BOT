from urllib import request
import urllib
from Credentials.Test.main_credentials_test import api_test
import tweepy

timeline = tweepy.Cursor(api_test.user_timeline, tweet_mode='extended').items()

for tweet in timeline:
    print(tweet)
    if 'media' in tweet.entities:
        for media in range(1):
            for media in tweet.extended_entities['media']:
                print(media['media_url'])
                urllib.request.urlretrieve(media['media_url'], "TESTE_PHILOMAKER.png")
        break
