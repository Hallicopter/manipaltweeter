#!/bin/env
import tweepy

auth=tweepy.OAuthHandler('Secret Auth key')

auth.set_access_token('Secret auth stuff', 'secret auth stuff')


api = tweepy.API(auth)

'''results= api.search(q='manipal', geocode='13.3525,74.7928,10km', rpp='100')


for tweet in results:
    encoded = tweet.text.encode("utf-8", errors='ignore')
    print(encoded)
    encoded = tweet.author.name.encode("utf-8", errors='ignore')
    print(encoded)
    print()'''

def retweetmanipal():
    for tweet in tweepy.Cursor(api.search,
                               q="manipal",
                               geocode='13.3525,74.7928,10km',
                               count=3,
                               result_type="recent",
                               include_entities=True,
                               lang="en").items(1):
        #print(tweet.text.encode("utf-8", errors='ignore'))
        #print(tweet.author.name.encode("utf-8", errors='ignore'))
        api.retweet(tweet.id)

#print("Test")
retweetmanipal()
