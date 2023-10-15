from google.auth.transport.requests import Request
import os
from googleapiclient.discovery import build
import googleapiclient.discovery
import googleapiclient.errors
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint
from google.oauth2.credentials import Credentials


class Youtube_Comment:

 def __init__(self):
  with open("credentials.json","r") as cred:
   credent = cred.read()
   cred.close()
  self.CLIENT_SECRET_FILE = credent
  self.SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
  self.api_key = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk"
  self.youtube = build('youtube', 'v3', developerKey=self.api_key)
  self.API_SERVICE_NAME = 'youtube'
  self.API_VERSION = 'v3'

 def get_channel_id(self, channel_name):
  self.request = self.youtube.channels().list(part="id", forUsername=channel_name)
  self.response = self.request.execute()
  if 'items' in self.response and len(self.response['items']) > 0:
   channel_id = self.response["items"][0]["id"]
   print(f"\nthe id of the {channel_name} channel is {channel_id}.\n") #   print (self.response)
   return channel_id
  else:
        raise ValueError("Channel not found")

 def get_latest_playlist_id(self, channel_id):
#   channels_response = self.youtube.channels().list(part="contentDetails",id=channel_id).execute()
   channels_response = self.youtube.channels().list(part="contentDetails",id=channel_id).execute()
   if 'items' in channels_response and len(channels_response['items']) > 0:
#         playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
         playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
         print(f"\nthe playlist id of the {channel_id} channel id is {playlist_id}.\n")
         return playlist_id
   else:
        raise ValueError("Playlist not found")

 def get_latest_video_id(self, playlist_id):
   playlistitems_response = self.youtube.playlistItems().list(part="snippet",playlistId=playlist_id,maxResults=1).execute()
   if 'items' in playlistitems_response and len(playlistitems_response['items']) > 0:
         video_id = playlistitems_response["items"][0]["snippet"]["resourceId"]["videoId"]
         print(f"\nthe video id of the {playlist_id} playlist is {video_id}.\n")
         return video_id
   else:
        raise ValueError("Video not found")
 def authenticate(self):
    creds = None
    if os.path.exists('token.json'):
      creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
 def authenticate1(self):
    creds = None
    if os.path.exists('token1.json'):
      creds = Credentials.from_authorized_user_file('token1.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token1.json', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
 def authenticate2(self):
    creds = None
    if os.path.exists('token2.json'):
      creds = Credentials.from_authorized_user_file('token2.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token2.json', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
 def authenticate3(self):
    creds = None
    if os.path.exists('token3.json'):
      creds = Credentials.from_authorized_user_file('token3.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token3.json', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
 def authenticate4(self):
    creds = None
    if os.path.exists('token4.json'):
      creds = Credentials.from_authorized_user_file('token4.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token4.json', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
 def authenticate5(self):
    creds = None
    if os.path.exists('token5.json'):
      creds = Credentials.from_authorized_user_file('token5.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token5.json', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
 def logo(self):
  print (f"""
{os.system('figlet -c -f banner Youtube | lolcat')}\n{os.system('figlet -c -f banner Commenter | lolcat')}
 for help : [info not availabe yet]

        """)
 def post_comment(self, video_id, comment_text):
    try:
        response = self.service.commentThreads().insert(
            part='snippet',
            body=dict(
                snippet=dict(
                    channelId='',
                    videoId=video_id,
                    topLevelComment=dict(
                        snippet=dict(
                            textOriginal=comment_text
                        )
                    )
                )
            )
        ).execute()

        comment_response = response['snippet']['topLevelComment']['snippet']
        comment_info = {
            'author': comment_response['authorDisplayName'],
            'text': comment_response['textDisplay'],
            'date': comment_response['publishedAt'],
            'like_count': comment_response['likeCount'],
            'comment_id': response['id']
        }
        return comment_info
    except HttpError as error:
        print('An error occurred: %s' % error)
        return None
 def reply_to_comment(self, video_id, comment_id, comment_text):
    try:
        response = self.service.comments().insert(
            part="snippet",
            body={
                "snippet": {
                    "parentId": comment_id,
                    "textOriginal": comment_text,
                    "videoId": video_id
                }
            }
        ).execute()
        reply_id = response['id']
        print(f"replied to comment {comment_id} with reply id {reply_id}")
    except HttpError as error:
        print('An error occurred: %s' % error)
 def get_link(self, video_id, comment_id, channel_id):
  comment_link = f"https://www.youtube.com/watch?v={video_id}&lc={comment_id}&ab_channel={channel_id}"
  return comment_link
 def run(self):
  self.logo()
  channel_name = input("Enter channel_name:\t")
  channel_id = self.get_channel_id(channel_name)
  playlist_id = self.get_latest_playlist_id(channel_id)
  video_id = self.get_latest_video_id(playlist_id)
  if __name__ == '__main__':
    self.service = self.authenticate()
    self.service1 = self.authenticate1()
    self.service2 = self.authenticate2()
    self.service3 = self.authenticate3()
    self.service4 = self.authenticate4()
    self.service5 = self.authenticate5()
#    self.service6 = self.authenticate6()
  comment_text = open("comment.txt").read()
  comment_info = self.post_comment(video_id, comment_text)
  comment_id = comment_info["comment_id"] # "Ugx_ssugU5o2urEUH0x4AaABAg" #comment_info["comment_id"]
  link = self.get_link(video_id, comment_id, channel_id)
  reply_id = self.reply_to_comment(video_id, comment_id, comment_text)
  links = self.get_link(video_id, reply_id, channel_id)
  print(f"\n[-] {links}")
  print(f"\n[=] {reply_id}")
  print(f"\n[+] {comment_info}")
  print(f"\n[-] {link}\n")
my_comment= Youtube_Comment()
my_comment.run()
