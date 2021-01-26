import tweepy
from time import sleep
import requests

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET =''
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def tweet(str):
  path = '/home/runner/Khediras-contract-expire/k.jpg'
  api.update_with_media(path,status=str)
  print('done')