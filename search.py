import oauth2 as oauth
import time
import json

http_method="GET"
post_body=None
http_headers=None

CONSUMER_KEY    = ""
CONSUMER_SECRET = ""
ACCESS_KEY      = ""
ACCESS_SECRET   = ""

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

words = ["happy"]

for word in words:
    next_results = -1
    while next_results!=0:

        try:

            if next_results==-1:
                timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q="+word+"&count=100"
            else:
                timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json"+next_results

            print timeline_endpoint

            response, data = client.request(timeline_endpoint)
            print response
            print data

            if response['status']=='200':
                if int(response['x-rate-limit-remaining'])<2:
                    time.sleep(int(response['x-rate-limit-reset'])-int(time.time()))

                data = json.loads(data)
                tweets = data['statuses']
                metadata = data['search_metadata']
                print metadata
                if 'next_results' in metadata:
                    next_results = metadata['next_results']
                    for tweet in tweets:
                        print tweet
                        created=tweet['created_at']
                    print created
                else:
                    next_results=0

                    time.sleep((15*60)/int(response['x-rate-limit-limit']))

            elif response['status']==400 or response['status']==403 or response['status']==404 or response['status']==401:
                print response['status']
            else:
                print response['status']

        except Exception,e:
            print 'exeption '+str(e)
            time.sleep(60)
