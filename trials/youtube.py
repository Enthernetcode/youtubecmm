from googleapiclient.discovery import build
import time, os
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk" #"YOUR_API_KEY_HERE"

def get_channel_id(channel_name):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)
    request = youtube.channels().list(part="id", forUsername=channel_name)
    response = request.execute()
    print (response)
    return response["items"][0]["id"]

#channel_id = get_channel_id("CHANNEL_NAME")
#print(channel_id)
def comment():
  with open("comments", "a+") as f:
    comment = f.read()
    f.close()
    return comment
def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)
with open("comment.txt", "r") as f:
 comment = f.read()
 f.close()
def post_comment(video_id, comment):
    youtube = authenticate()
    request = youtube.commentThreads().insert(
        part='snippet',
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {
                    "snippet": {
                        "textOriginal": comment
                    }
                }
            }
        }
    )
    response = request.execute()
    print("Comment posted successfully!")

channel_username = input('ENTER YOUR_CHANNEL_USERNAME:\t')
channel_id = get_channel_id(channel_username)

def post_comment_on_channel_videos(channel_id, comment):
    youtube = authenticate()
    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        order='date',
        type='video'
    )
    response = request.execute()
    video_ids = [item['id']['videoId'] for item in response['items']]  
    for video_id in video_ids:
        post_comment(video_id, comment)

channel_id = 'YOUR_CHANNEL_ID'
comment = comment # 'Your comment here.'
post_comment_on_channel_videos(channel_id, comment)
