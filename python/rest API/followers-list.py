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

users=['jack']

for user in users:

    next_cursor=-1
    while next_cursor!=0:

        if next_cursor<0:
            timeline_endpoint = "https://api.twitter.com/1.1/followers/list.json?count=200&cursor=-1&screen_name="+user+"&skip_status=true&include_user_entities=true"

        else:
            timeline_endpoint = "https://api.twitter.com/1.1/followers/list.json?count=200&cursor="+str(next_cursor)+"&screen_name="+user+"&skip_status=true&include_user_entities=true";

        print timeline_endpoint
        try:
            response, data = client.request(timeline_endpoint)
            print response
            print data
            if response['status']=='200':
                if int(response['x-rate-limit-remaining'])<2:
                    print 'id rescue: wait '+str(int(response['x-rate-limit-reset'])-int(time.time()))+' seconds'
                    time.sleep(int(response['x-rate-limit-reset'])-int(time.time()))

                dataResult = json.loads(data)

                next_cursor = dataResult['next_cursor']

                for userFollower in dataResult['users']:
                    print userFollower

                print 'id rescue: wait '+str((15*60)/int(response['x-rate-limit-limit']))+' seconds'
                time.sleep((15*60)/int(response['x-rate-limit-limit']))

            elif response['status']==400 or response['status']==403 or response['status']==404 or response['status']==401:
                print response['status']
                next_cursor=0
            else:
                print response['status']
                next_cursor=0

        except Exception,e:
            print 'exeption '+str(e)
            time.sleep(60)

