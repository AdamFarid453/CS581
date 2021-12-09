"""
    Python program to to retrieve some data from the Twitter API,
    and do some processing on that data
    Author: Adam Farid
"""

#  To run in a terminal window:   python3  farid.py

#imports
import tweepy
import re

# AUTHENTICATOIN KEYS
CONSUMER_KEY = "QXTTrAl9jxVnwSWQLFqQ3lBq5"
CONSUMER_KEY_SECRET = 'Y4S2eHYfstAY5MVj3nwN1KGWC1UUf46heclYqQ1geiI9wdQnsv'
ACCESS_TOKEN = '1145537323003781122-KYQWUnWzUywibvLxuS7fwMx2jzaTxo'
ACCESS_TOKEN_SECRET = '4LzprQLB6oAQQToDQZwZwngLF6EkdAM0VvBXqo3YI8AQR'

# Authentication
authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(authenticate)



def main(input):    
    twitter_user = api.get_user(screen_name = userInput)

    # Print the User Screen Name
    print("User Screen Name: " + userInput)
    # Print the User's Name
    print("User Name: " + twitter_user.name)
    # Print the User's ID
    print("User ID: " + str(twitter_user.id))
    # Print the User's Description
    print("User Description: " + twitter_user.description)
    # Print the Location
    print("User Location: " + twitter_user.location)
    # Print the User's Friends with a thousand separator
    print("User Friends: " + str('{:,}'.format(twitter_user.friends_count))) 
    # Print the User's Followers with a thousand separator
    print("User Followers: " + str('{:,}'.format(twitter_user.followers_count)) +"\n")
    # Print the screen names of the most recent 5 followers of the Twitter User Account, with appropriate label
    print("User's 5 most recent followers: ")
    # If user has less than 5 followers, print an error message
    if twitter_user.followers_count < 5:
        print("Error: User has less than 5 followers \n")
    for follower in twitter_user.followers()[0:5]:
        print(follower.screen_name)  
    
    #Print the text of the Twitter User Account's most recent 5 tweets.  Label each as TWEET 1, TWEET 2,  etc., with a blank line between tweets 
    print("\nUser's 5 most recent tweets: \n")
    # If user has less than 5 tweets, print an error message
    if twitter_user.statuses_count < 5:
        print("Error: User has less than 5 tweets \n")
    tweetNumber=1
    for tweet in twitter_user.timeline()[0:5]:
        print("TWEET " + str(tweetNumber) + ": " + tweet.text) 
        tweetNumber += 1 
        print("\n")

# Python main method
if __name__ == '__main__':
    # Prompting the user for a Twitter User Screen Name.  If the user enters STOP, end the program with an appropriate message and stop.
    # If the user enters a valid Twitter User Screen Name, continue.
    userInput = input("Enter a Twitter User Screen Name: ")
    while userInput != "STOP":
        # check for a valid twitter User Screen Name, and print an error message and ask again.
        pattern = re.compile("^[a-zA-Z0-9_]{1,15}$") #regex for valid twitter User Screen Name
        if pattern.match(userInput) == None: # if the user input does not match the regex, print an error message and ask again.
            print("Invalid Twitter User Screen Name.  Please try again.")
            userInput = input("Enter a Twitter User Screen Name: ")
            if userInput == "STOP":
                print("\nThank you for using the Twitter Bot.  Have a nice day!")
                exit()
        main(userInput) 
        userInput = input("Enter a Twitter User Screen Name: ")
    print("\nThank you for using the Twitter Bot.  Have a nice day!")
    exit()

    
    

