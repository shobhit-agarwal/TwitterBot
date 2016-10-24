__author__ = 'vipulvaibhaw'
import time
import WeatherBotFunctions
import Keys
import thread
from twitter import *

WeatherBot_Keys = Keys.WeatherBot()

#Weather Bot Authentication Keys.
con_secret = WeatherBot_Keys.con_secret()
con_secret_key = WeatherBot_Keys.con_secret_key()
token = WeatherBot_Keys.token()
token_key = WeatherBot_Keys.token_key()

t = Twitter(
auth=OAuth(token, token_key, con_secret, con_secret_key))

def NewTweetCheckerThread(delay):
    if k.CheckForNewTweets() == True:
        print "Ok Analysing the tweets!"
        for i in range(0,k.count):
            tweettype = k.AnalyseIncomingTweet(i)
            print tweettype
            print k.ReplyTweet(tweettype)
            time.sleep(5)
        print "done"
    time.sleep(delay)


while True:
    k = WeatherBotFunctions.Functions(t)
    NewTweetCheckerThread(15)

