__author__ = 'vipulvaibhaw'

import time
import QuoteBotFunctions
from Keys import RandomQuoteTweeterBot
from twitter import *

#Quote Bot Authentication Keys.
con_secret = RandomQuoteTweeterBot().con_secret()
con_secret_key = RandomQuoteTweeterBot().con_secret_key()
token = RandomQuoteTweeterBot().token()
token_key = RandomQuoteTweeterBot().token_key()

t = Twitter(
auth=OAuth(token, token_key, con_secret, con_secret_key))

def QuoteTweeterThread(delay):
    print k.RandomQuoteTweeter()
    time.sleep(delay)

while True:
    k = QuoteBotFunctions.Functions(t)
    QuoteTweeterThread(300)