__author__ = 'vipulvaibhaw'

import urllib2
from bs4 import BeautifulSoup
import Keys
import re

class Book:
    def __init__(self,title):
        goodreads = Keys.GoodReads()
        self.title = title
        self.url1 = "https://www.goodreads.com/book/title/?format=xml&key="
        self.url2 = "&title="
        self.finalurl = self.url1+goodreads.key()+self.url2+self.title
        page = urllib2.urlopen(self.finalurl)
        soup = BeautifulSoup(page)
        self.author_name = soup.find("name")
        self.average_rating = soup.average_rating

    def KnowRating(self):
        return self.average_rating.text

    def Author(self):
        return ''.join(re.sub(r'[?|$|.|!]',r"",self.author_name.text).split(" "))

#k = Book("harry%20potter?")
#print str(k.KnowRating()) + "yes! "
#print k.Author()

"""strs = "how much for the maple syrup? $20.99? That's ricidulous!!!"
print strs
nstr = re.sub(r'[?|$|.|!]',r'',strs)
print nstr
nestr = re.sub(r'[^a-zA-Z0-9 ]',r'',nstr)
print nestr"""