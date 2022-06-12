import tweepy
import requests
import json
import time


CONSUMER_KEY = "#"
CONSUMER_SECRET =  "#"
ACCESS_TOKEN = "#"
ACCESS_TOKEN_SECRET = "#"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


print('logged in succesfully')

while True:
    etherprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
    price = etherprice.json()
    ethusd = price['ethereum']['usd']
    

    message = 'Current #Ethereum Price: ' + str(ethusd) + ' USD\n'
    api.update_status(message)
    print("Ethereum:$", ethusd)
    print('tweet was posted')
    time.sleep(3600)
    


