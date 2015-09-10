__author__ = 'mirko'
import oauth2 as oauth
import time
import json

CONSUMER_KEY    = ""
CONSUMER_SECRET = ""
ACCESS_KEY      = ""
ACCESS_SECRET   = ""

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

users = ["jack"]

for user in users:


    place_endpoint = "https://api.twitter.com/1.1/users/show.json?screen_name="+user

    response, data = client.request(place_endpoint)
    print response
    print response['status']
    print response['x-rate-limit-limit']
    print data
    if response['status']=='200':
        if int(response['x-rate-limit-remaining'])<2:
            print 'id rescue: wait '+str( int(response['x-rate-limit-reset']) - int(time.time()) )+' seconds'
            time.sleep(int(response['x-rate-limit-reset'])-int(time.time()))

    jsonTweet=json.loads(data)
    print json.dumps(jsonTweet,2)
    print 'id rescue: wait '+str((15*60)/int(response['x-rate-limit-limit']))+' seconds'
    time.sleep((15*60)/int(response['x-rate-limit-limit']))
