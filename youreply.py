
from googleapiclient.discovery import build
import os
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

class Youtubereply:
 def __init__(self, video_id, comment_id):
   with open("credentials.json","r") as cred:
    credent = cred.read()
    cred.close()
   self.api_key = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk"
   self.CLIENT_SECRET_FILE = credent
   self.SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
   self.api_key = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk"
   self.youtube = build('youtube', 'v3', developerKey=self.api_key)
   self.API_SERVICE_NAME = 'youtube'
   self.API_VERSION = 'v3'
 def authenticate(self):
    creds = None
    if os.path.exists('token.json'):
      creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)

 def reply_comment(self, comment_id, comment_text):
    try:
        comment_thread_snippet = {
    'snippet': {
        'videoId': comment_id,
        'topLevelComment': {
            'snippet': {
                'textOriginal': comment_text
            }
        }
    }
}
        response = self.youtube.commentThreads().insert(
        part='snippet',
        body=comment_thread_snippet
    ).execute()
        reply_id = response["id"]
        print (reply_id)
        print(f'Comment {comment[snippet][textOriginal]} was posted on {comment_id}.')
        return response
    except HttpError as error:
        print(f'An error occurred: {error}')
 def run(self):
    service = self.authenticate()
    reply = self.reply_comment(comment_id, comment_text)

comment_id = input("Enter comment_id>> ")
comment_text = input("Enter comment_text>> ")
my_comment = Youtubereply(comment_id, comment_text)
my_comment.run()
