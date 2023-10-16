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
  self.channel_id = input("channel id >>")
  self.playlist_id = input("playlist id >>")
  self.video_id = input("video id >>")
  self.comment_id = input("comment id >>")
 def authenticate(self):
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
        with open('token.json4', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
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
 def run(self):
  channel_id = self.channel_id
  playlist_id = self.playlist_id
  video_id = self.video_id
  if __name__ == '__main__':
    self.service = self.authenticate()
  comment_text = open("comment.txt").read()
  comment_id = self.comment_id
  reply_id = self.reply_to_comment(video_id, comment_id, comment_text)
#  links = self.get_link(video_id, reply_id, channel_id)
#  print(f"\n[-] {links}")
  print(f"\n[=] {reply_id}")
#  print(f"\n[+] {comment_info}")
#  print(f"\n[-] {link}\n")
my_comment= Youtube_Comment()
my_comment.run()
