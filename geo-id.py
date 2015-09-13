__author__ = 'mirko'
import sys
import time
import oauth2 as oauth
import json


CONSUMER_KEY    = ""
CONSUMER_SECRET = ""
ACCESS_KEY      = ""
ACCESS_SECRET   = ""

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
clientTwitter = oauth.Client(consumer, access_token)

places_id=['419060023b8455e1']

for place_id in places_id:

    try:
            place_endpoint = "https://api.twitter.com/1.1/geo/id/"+place_id+".json"
            response, data = clientTwitter.request(place_endpoint)


            if response['status']=='200':
                if int(response['x-rate-limit-remaining'])<2:
                    print 'Reverse Geocoding: wait '+str( int(response['x-rate-limit-reset']) - int(time.time()) )+' seconds'
                    time.sleep(int(response['x-rate-limit-reset'])-int(time.time()))

                result=json.loads(data)



                codes = result['attributes']['174368:admin_order_id']

                print codes

            print ': wait 60 seconds'
            time.sleep((15*60)/int(response['x-rate-limit-limit']))

    except:
        print "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1]
