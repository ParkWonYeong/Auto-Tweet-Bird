import tweepy
from Token import * #Call Twitter API from Token.py

# Written from ___
#AK= "" 
#AKS = ""

# User ID
#AT = ""
#ATS = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(AK, AKS)
auth.set_access_token(AT, ATS)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)