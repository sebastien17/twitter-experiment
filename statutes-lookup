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

#all list of id you want to retrieve
myList = ['20']

while len(myList) > 0:
        parameter = ','.join(myList[0:99]) #max 100 id per request
        myList[0:99] =[]
        try:
            place_endpoint ="https://api.twitter.com/1.1/statuses/lookup.json?id="+parameter
            response, data = client.request(place_endpoint)
            if response['status']=='200':
                if int(response['x-rate-limit-remaining'])<2:
                    print 'id rescue: wait '+str( int(response['x-rate-limit-reset']) - int(time.time()) )+' seconds'
                    time.sleep(int(response['x-rate-limit-reset'])-int(time.time()))

            jsonTweet=json.loads(data)
            for tweet in jsonTweet:
                print json.dumps(tweet)

            print 'id rescue: wait '+str((15*60)/int(response['x-rate-limit-limit']))+' seconds'
            time.sleep((15*60)/int(response['x-rate-limit-limit']))
        except Exception, e:
            print e
