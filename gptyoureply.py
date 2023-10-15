from googleapiclient.discovery import build
import os
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Youtubereply:
    def __init__(self, api_key, video_id, comment_id):
        self.api_key = api_key
        self.video_id = video_id
        self.comment_id = comment_id
        self.CLIENT_SECRET_FILE = "credentials.json"
        self.SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
        self.youtube = self.authenticate()

    def authenticate(self):
        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CLIENT_SECRET_FILE, self.SCOPES)
                credentials = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(credentials.to_json())
        youtube = build('youtube', 'v3', developerKey=self.api_key, credentials=credentials)
        return youtube

    def reply_comment(self, comment_id, comment_text):
        try:
            comment_thread_snippet = {
                'snippet': {
                    'videoId': self.video_id,
                    'topLevelComment': {
                        'snippet': {
                            'parentId': comment_id,
                            'textOriginal': "Nice am glad"
                        }
                    }
                }
            }
            response = self.youtube.comments().insert(part='snippet', body=comment_thread_snippet).execute()
            reply_id = response['id']
            print(f"Reply to comment ID '{comment_id}' successful. Reply ID: '{reply_id}'")
            print(f"Reply Text: {comment_text}")
        except HttpError as e:
            print(f"An error occurred while replying to comment ID '{comment_id}':")
            print(f"Error message: {str(e)}")

#           response = self.youtube.commentThreads().insert(
#            part='snippet',
#            body=dict(
#                snippet=dict(
#                    channelId='',
#                    videoId=video_id,
#                    parentId=comment_id,
#                    topLevelComment=dict(
#                        snippet=dict(
#                            textOriginal=comment_text
#                        )
#                    )
#                )
#            )
#           ).execute()
#
#           comment_response = response['snippet']['topLevelComment']['snippet']
#           comment_info = {
#            'author': comment_response['authorDisplayName'],
#            'text': comment_response['textDisplay'],
#            'date': comment_response['publishedAt'],
#            'like_count': comment_response['likeCount'],
#            'comment_id': response['id']
#            }
#           return comment_info
#        except HttpError as error:
#           print('An error occurred: %s' % error)
#           return None
    def run(self):
        comment_text = input("Enter the reply text: ")
        info = self.reply_comment(self.comment_id, comment_text)
        print = ("{info}")

api_key = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk"
video_id = input("Enter VIDEO_ID>> ")
comment_id = input("Enter COMMENT_ID>> ")
youtube_reply = Youtubereply(api_key, video_id, comment_id)

youtube_reply.run()

