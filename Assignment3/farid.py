"""
    Python program to retrieve and process data from the YouTube API
    Author: Adam Farid
"""

# To run this file, make sure you are in the right directory and run python3 farid.py
# Then supply the program with the inputs provided by the instructions in the console

# global imports
from time import sleep
from tabulate import tabulate
from googleapiclient.discovery import build
import csv
import re
import isodate
import datetime

# API data
API_KEY = "AIzaSyDE1fGwKUiZx5oFdtoWHIFXR6HazS7sIKs"
API_NAME = "youtube"
API_VERSION = "v3"

# Prompting User for input
print("Please enter in a Seach Term")
search_term = input()
print("Please enter in a Max Number of Results")
search_max = input()
print(f"Finding videos matching the term '{search_term}', and search max of {search_max}.\n")

# API calls
youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
search_data = youtube.search().list(q=search_term, part="id,snippet", maxResults=search_max).execute()

# initializing data to print to console later
analysis_one_data = []
analysis_two_data = []
analysis_three_data = []
rank = 0

#  retrieve the YouTube records matching search term and max
for search_instance in search_data.get("items", []):
    if search_instance["id"]["kind"] == "youtube#video":

        # Grabbing the field values from the API call
        videoId = search_instance["id"]["videoId"]  
        title = search_instance["snippet"]["title"] 
        video_data = youtube.videos().list(id=videoId,part="statistics").execute()
        duration = youtube.videos().list(id=videoId,part="contentDetails").execute()

        # Grabbing the duration and converting to seconds using the date time library
        vidDuration = duration["items"][0]["contentDetails"]["duration"]
        dur = isodate.parse_duration(vidDuration)
        totalDuration = datetime.timedelta(seconds=dur.total_seconds())

        for video_instance in video_data.get("items",[]):
            viewCount = int(video_instance["statistics"]["viewCount"])
            if 'likeCount' not in video_instance["statistics"]:
                likeCount = 0
            else:
                likeCount = int(video_instance["statistics"]["likeCount"])
            if 'dislikeCount' not in video_instance["statistics"]:
                dislikeCount = 0
            else:
                dislikeCount = int(video_instance["statistics"]["dislikeCount"])
        if viewCount == 0:
            like_rank = 0
            dislike_rank = 0
        else:
            like_rank = (likeCount / viewCount) * 100
            dislike_rank = (dislikeCount / viewCount) * 100
        #Appending all the data grabbed by the API to the array
        analysis_one_data.append([videoId, "{:,d}".format(viewCount), "{:,d}".format(likeCount), "{:,d}".format(dislikeCount),totalDuration, title])
        analysis_two_data.append([rank,'%.3f'%like_rank ,videoId, "{:,d}".format(viewCount), "{:,d}".format(likeCount), "{:,d}".format(dislikeCount),totalDuration, title])
        analysis_three_data.append([rank,'%.3f'%dislike_rank ,videoId, "{:,d}".format(viewCount), "{:,d}".format(likeCount), "{:,d}".format(dislikeCount),totalDuration, title])
        
# Sorting the arrays by rank
analysis_two_data = sorted(analysis_two_data, key=lambda x: x[1], reverse=True)
analysis_three_data = sorted(analysis_three_data, key=lambda x: x[1], reverse=True)

#update rank for both analysis
for newRank in range(len(analysis_two_data)):
    analysis_two_data[newRank][0] = newRank+1
    analysis_three_data[newRank][0] = newRank+1
# create header
analysis_one_head = ["ID", "Views", "Likes", "Dislikes","Duration", "Title"]
analysis_two_head = ["Rank","Like Percentage" ,"ID", "Views", "Likes", "Dislikes","Duration", "Title"]
analysis_three_head = ["Rank","Dislike Percentage" ,"ID", "Views", "Likes", "Dislikes","Duration", "Title"]

# display table
print(tabulate(analysis_one_data, headers=analysis_one_head, tablefmt="grid"), "\n")
print(tabulate(analysis_two_data, headers=analysis_two_head, tablefmt="grid"), "\n")
print(tabulate(analysis_three_data, headers=analysis_three_head, tablefmt="grid"), "\n")
print("Excel file has been updated!")

# Creating and storing contents of the First Analysis into the Excel File
with open('youtube_analysis.csv', 'w', encoding='UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(analysis_one_head)
    for row in analysis_one_data:
        writer.writerow(row)
    