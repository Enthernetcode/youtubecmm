from google.auth.transport.requests import Request
import os
from googleapiclient.discovery import build
import googleapiclient.discovery
import googleapiclient.errors
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from pprint import pprint
from google.oauth2.credentials import Credentials

class Youtube_Comment:

 def __init__(self):
    self.CLIENT_SECRET_FILE = "credentials.json"
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
        print(f"\nthe id of the {channel_name} channel is {channel_id}.\n")
        return channel_id
    else:
        raise ValueError("Channel not found")

 def get_latest_playlist_id(self, channel_id):
    channels_response = self.youtube.channels().list(part="contentDetails", id=channel_id).execute()
    if 'items' in channels_response and len(channels_response['items']) > 0:
        playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        print(f"\nthe playlist id of the {channel_id} channel id is {playlist_id}.\n")
        return playlist_id
    else:
        raise ValueError("Playlist not found")

 def get_latest_video_id(self, playlist_id):
    playlistitems_response = self.youtube.playlistItems().list(part="snippet", playlistId=playlist_id,
                                                               maxResults=1).execute()
    if 'items' in playlistitems_response and len(playlistitems_response['items']) > 0:
        video_id = playlistitems_response["items"][0]["snippet"]["resourceId"]["videoId"]
        print(f"\nthe video id of the {playlist_id} playlist is {video_id}.\n")
        return video_id
    else:
        raise ValueError("Video not found")

 def get_authenticated_service(self):
    flow = InstalledAppFlow.from_client_secrets_file(self.CLIENT_SECRET_FILE, self.SCOPES)
    credentials = flow.run_console()
    return build('youtube', 'v3', credentials=credentials)

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

 def logo(self):
    os.system('figlet -c -f banner Youtube | lolcat')
    os.system('figlet -c -f banner Commenter | lolcat')
    print("for help: [info not available yet]\n")

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

 def get_link(self, video_id, comment_id, channel_id):
    comment_link = f"https://www.youtube.com/watch?v={video_id}&lc={comment_id}&ab_channel={channel_id}"
    return comment_link

 def reply_to_comment(self, video_id, comment_id, comment_text):
#    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json',
#                                                     scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
#    credentials = flow.run_local_server(port=8080)
#    youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)
#    comment_thread_snippet = {'snippet': {'videoId': comment_id, 'topLevelComment': {'snippet': {'textOriginal': comment_text}}}}
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
    except HttpError as error:
        print('An error occurred: %s' % error)

 def run(self):
    self.logo()
    channel_name = input("Enter channel_name:\t")
    channel_id = self.get_channel_id(channel_name)
    playlist_id = self.get_latest_playlist_id(channel_id)
    video_id = self.get_latest_video_id(playlist_id)
    self.service = self.authenticate()
    comment_text = open("comment.txt").read()
    comment_info = self.post_comment(video_id, comment_text)
    comment_id = comment_info["comment_id"]
    link = self.get_link(video_id, comment_id, channel_id)
    reply = self.reply_to_comment(video_id, comment_id, comment_text)
    print(f"[=] {reply}")
    print(f"[+] {comment_info}")
    print(f"\n[-] {link}\n")

my_comment = Youtube_Comment()
my_comment.run()
