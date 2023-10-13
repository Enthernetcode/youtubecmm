from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

creds_file = '/data/data/com.termux/files/home/youtubecmm/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
api_key = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk"
#youtube = build('youtube', 'v3', developerKey=self.api_key)
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
credentials = Credentials.from_authorized_user_file(creds_file)
#with open("credentials.json","r") as cred:
#  info = cred.read()
#  cred.close()
#credentials = Credentials.from_authorized_user_info(info)
youtube = build('youtube', 'v3', credentials=credentials)
response = youtube.comments().list(
       part='snippet',
       id='UgzAuAFyVl3bKlfZwFl4AaABAg' #COMMENT_ID'
   ).execute()
video_id = response['items'][0]['snippet']['videoId']
comment_id = response['items'][0]['id']
author_channel_id = response['items'][0]['snippet']['authorChannelId']['value']
body = {
       'snippet': {
           'parentId': comment_id,
           'textOriginal': 'Your reply here',
           'channelId': author_channel_id
       }
   }
response = youtube.comments().insert(
       part='snippet',
       body=body
   ).execute()
