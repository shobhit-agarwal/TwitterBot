__author__ = 'vipulvaibhaw'

import AdvancedMessageConstructor
import random

class Functions():
    def __init__(self,t):
        self.t = t

    def RandomQuoteTweeter(self):
        try:
            m = AdvancedMessageConstructor.Messages(None)
            fw = open('quotes.txt','r')
            vocab = fw.read()
            vocab = vocab.split('\n')
            i = random.randint(0,2002)
            if i % 2 == 0:
                if len(vocab[i]) < 118:
                    name =  vocab[i+1].strip(".").split(" ")
                    finalname =  ''.join(name)
                    message = m.RandomQuoteTweeterMessage(vocab[i],finalname)
                    self.t.statuses.update(status=message)
                    return "Tweeted " + message
        except Exception,e: return str(e)