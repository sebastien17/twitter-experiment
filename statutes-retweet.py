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

ids_str=['20']

for id_str in ids_str:

    max_id=-1
    while max_id!=0:

        if max_id<0:

            timeline_endpoint = "https://api.twitter.com/1.1/statuses/retweets/"+id_str+".json"
        else:
            timeline_endpoint = "https://api.twitter.com/1.1/statuses/retweets/"+id_str+".json?max_id="+str(max_id)

        print timeline_endpoint
        try:
            response, data = client.request(timeline_endpoint)
            print response
            if response['status']=='200':
                if int(response['x-rate-limit-remaining'])<2:
                    print 'id rescue: wait '+str(int(response['x-rate-limit-reset'])-int(time.time()))+' seconds'
                    time.sleep(int(response['x-rate-limit-reset'])-int(time.time()))

                max_id = 0
                tweets = json.loads(data)

                for tweet in tweets:
                    print tweet
                    if max_id==0:
                        max_id=int(tweet['id'])
                    elif max_id>int(tweet['id']):
                        max_id=int(tweet['id'])-1
                    created=tweet['created_at']
                print created
                print 'id rescue: wait '+str((15*60)/int(response['x-rate-limit-limit']))+' seconds'
                time.sleep((15*60)/int(response['x-rate-limit-limit']))

            elif response['status']==400 or response['status']==403 or response['status']==404 or response['status']==401:
                print response['status']
                max_id=0
            else:
                print response['status']
                max_id=0

        except Exception,e:
            print 'exeption '+str(e)
            time.sleep(60)

