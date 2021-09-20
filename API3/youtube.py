# Author:  Cheryl Dugas

#youtube.py searches YouTube for videos matching a search term and max results
from googleapiclient.discovery import build      # use build function to create a service object


API_KEY = "AIzaSyDE1fGwKUiZx5oFdtoWHIFXR6HazS7sIKs"

API_NAME = "youtube"
API_VERSION = "v3"  
#  retrieve the YouTube records matching search term and max

search_term = "computer"
search_max = 5

youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

search_data = youtube.search().list(q=search_term, part="id,snippet", maxResults=search_max).execute()
    
# search for videos matching search term;
    
for search_instance in search_data.get("items", []):
    if search_instance["id"]["kind"] == "youtube#video":
        
        videoId = search_instance["id"]["videoId"]  
        title = search_instance["snippet"]["title"]
                      
                  
        video_data = youtube.videos().list(id=videoId,part="statistics").execute()
        for video_instance in video_data.get("items",[]):
            viewCount = video_instance["statistics"]["viewCount"]
            if 'likeCount' not in video_instance["statistics"]:
                likeCount = 0
            else:
                likeCount = video_instance["statistics"]["likeCount"]
                    
            
        print("")    
        print(videoId, title, viewCount, likeCount)
