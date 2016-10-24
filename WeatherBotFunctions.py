__author__ = 'vipulvaibhaw'

import weatherparser
import AdvancedMessageConstructor
import BookReviewParser
import re


class Functions():
    def __init__(self,t):
        self.t = t
        self.a = self.t.search.tweets(q="@theindianbot")
        self.k = len(self.a["statuses"])
        self.count = 0
        self.user_name = None

    def CheckForNewTweets(self):
        self.lines = open("twitterZ.txt", 'r').readlines()
        z = int(self.lines[0])
        print "\nEstablishing Connection...."
        print "\nChecking for new tweets....\n"
        if self.a["statuses"][0]["id"] == z:
            print "No New Tweets!"
            self.count = 0
            return False
        else:
            for i in range(0,self.k):
                if self.a["statuses"][i]["id"] != z:
                    self.count += 1
                elif self.a["statuses"][i]["id"] == z:
                    #update variable z here
                    lines = open("twitterZ.txt", 'r').readlines()
                    z = str(self.a["statuses"][0]["id"])
                    lines[0] = z
                    file = open("twitterZ.txt", 'w')#re-write first line of text file.
                    for line in lines:
                        file.write(line)
                    file.close()
                    break
            print "You have got "+str(self.count)+" new tweets."
            return True

    def AnalyseIncomingTweet(self,i):
        tweet =  self.a["statuses"][i]["text"].lower().split()
        self.user_name = str(self.a["statuses"][i]["user"]["screen_name"])
        #print tweet
        if len(tweet)==2:
            self.city_name = str(tweet[1])
            return "ProbablyOldFormat"
        if "book" in tweet:
            book_word_index = tweet.index("book")+1
            self.book_title_clean = re.sub(r'[?|$|.|!]',r'',' '.join(tweet[book_word_index:]))
            self.book_title = '%20'.join(self.book_title_clean.split(" "))
            print "Asking about Book - " + self.book_title
            return "BookInfo"
        if "weather" in tweet:
            self.city_name = str(tweet[tweet.index("weather")+2])
            print "Asking about Weather of "+ self.city_name
            return "WeatherInfo"
        if "thanks" in tweet or "thank" in tweet or "thanku" in tweet:
            print "@"+str(self.a["statuses"][i]["user"]["screen_name"])+" is thanking you."
            return "ThankYouNote"
        else:
            return "Failed to understand the tweet."

    def ReplyTweet(self,tweettype):
        if tweettype == "WeatherInfo":
            try:
                weather = weatherparser.Weather(self.city_name)
                dic = weather.Know()
                m = AdvancedMessageConstructor.Messages(self.user_name)
                message = m.WeatherMessage(self.city_name,dic["country"],dic["temperature"],dic["clouds"],dic["source"])
                self.t.statuses.update(status=message)
                return "Tweeted "+message
            except Exception,e: return str(e)
        if tweettype == "ThankYouNote":
            try:
                m = AdvancedMessageConstructor.Messages(self.user_name)
                message = m.ThankYouMessage()
                self.t.statuses.update(status=message)
                return "Tweeted "+message
            except Exception,e: return str(e)
        if tweettype == "ProbablyOldFormat":
            try:
                weather = weatherparser.Weather(self.city_name)
                dic = weather.Know()
                m = AdvancedMessageConstructor.Messages(self.user_name)
                message = m.WeatherMessage(self.city_name,dic["country"],dic["temperature"],dic["clouds"],dic["source"])
                self.t.statuses.update(status=message)
                return "Tweeted "+message
            except Exception,e: return str(e)
        if tweettype == "BookInfo":
            try:
                m = AdvancedMessageConstructor.Messages(self.user_name)
                message = m.BookRaterMessage(str(self.book_title_clean),str(self.book_title))
                self.t.statuses.update(status=message)
                return "Tweeted "+ message
            except Exception,e: return str(e)
        else:
            return "Didn't understand Your tweet."

