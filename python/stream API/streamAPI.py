__author__ = 'mirko'
# -*- coding: iso-8859-15 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import traceback
import logging
import codecs
import gzip
import os.path
import glob
from datetime import datetime
import shutil


consumer_key    = ""
consumer_secret = ""
access_token      = ""
access_token_secret   = ""

class StdOutListener(StreamListener):

    def on_data(self, tweet):

        try:

            jsonTweet=json.loads(tweet)
            if 'timestamp_ms' in jsonTweet:
                date = datetime.fromtimestamp(int(jsonTweet['timestamp_ms'])/1000)
                date = date.replace(minute=0, second=0, microsecond=0)
                date = date.strftime('%Y-%m-%d %H:%M:%S')

                if not os.path.isfile(date+'.out'):
                    for  file in glob.glob("*.out"):
                        with open(file, 'rb') as f_in, gzip.open(file+".gz", 'ab') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                        os.remove(file)

                file = codecs.open(date+'.out', "a", "utf-8")
                file.write(tweet)
                file.close()

            else:
                logging.debug(tweet)

            return True

        except Exception:
            logging.warning(traceback.format_exc())
            pass


    def on_error(self, status):
        logging.warning(traceback.format_exc())


if __name__ == '__main__':

    logging.basicConfig(filename='twitter_stream.log',level=logging.DEBUG)
    logging.debug('Start stream')

    try:
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=["music"])

    except Exception:
        logging.warning(traceback.format_exc())

