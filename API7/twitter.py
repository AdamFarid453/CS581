#   Author: Cheryl Dugas

#  This program accesses data from a twitter user site (hard-coded as Stevens)

#  To run in a terminal window:   python3  twitter.py


import tweepy

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "QXTTrAl9jxVnwSWQLFqQ3lBq5"
CONSUMER_KEY_SECRET = 'Y4S2eHYfstAY5MVj3nwN1KGWC1UUf46heclYqQ1geiI9wdQnsv'
ACCESS_TOKEN = '1145537323003781122-KYQWUnWzUywibvLxuS7fwMx2jzaTxo'
ACCESS_TOKEN_SECRET = '4LzprQLB6oAQQToDQZwZwngLF6EkdAM0VvBXqo3YI8AQR'

# Authentication
authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(authenticate)

# Get Information About a Twitter User Account

twitter_user = api.get_user(screen_name = 'FollowStevens')

# Get Basic Account Information
print("twitter_user id: ", twitter_user.id)

print("twitter_user name: ", twitter_user.name)

# Determine an Account’s Friends 
friends = []

print("\nFirst 5 friends:")

# Creating a Cursor
cursor = tweepy.Cursor(api.get_friends, screen_name='FollowStevens')

# Get and print 5 friends
for account in cursor.items(5):
    print(account.screen_name)
    