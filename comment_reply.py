from googleapiclient.discovery import build
import os

api_key = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk" 	#os.environ.get('YOUTUBE_API_KEY')  # Replace with your API key
youtube = build('youtube', 'v3', developerKey=api_key)

comment_id = input("comment id: ") #'UgypH_gFmOITDeE6CdV4AaABAg'
videoId = input("vid id: ") #"poDIT2ruQ9M&lc"
response = youtube.commentThreads().list(part='snippet', maxResults=1, videoId=comment_id).execute() # youtube.commentThreads().list(part='snippet', maxResults=1, searchTerms=comment_id).execute()

reply_to_comment_id = response['items'][0]['id']

reply_text = 'Thanks'

response = youtube.comments().insert(
    part='snippet',body={'snippet': {'parentId': reply_to_comment_id,'textOriginal': reply_text}}).execute()

reply_id = response['id']
