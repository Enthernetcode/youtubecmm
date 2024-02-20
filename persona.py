from google.auth.transport.requests import Request
import os
import csv
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
  with open("credentials1.json","r") as cred:
   credent = cred.read()
   cred.close()
  self.CLIENT_SECRET_FILE = credent
  self.SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
  self.api_key = "AIzaSyDjffdHgn-DV4U8TmzaeQXHlsqWHmadT9U"
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
 def authenticate6(self):
    creds = None
    if os.path.exists('token6.json'):
      creds = Credentials.from_authorized_user_file('token6.json', self.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token6.json', 'w') as token:
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
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service1.comments().insert(
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

 def reply_to_comment1(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
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
 def reply_to_comment2(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service2.comments().insert(
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
 def reply_to_comment3(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service3.comments().insert(
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
 def reply_to_comment4(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service2.comments().insert(
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
 def reply_to_comment5(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service3.comments().insert(
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
 def reply_to_comment6(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service2.comments().insert(
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
 def reply_to_comment7(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
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
 def reply_to_comment8(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
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
 def reply_to_comment9(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
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
 def reply_to_comment10(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service1.comments().insert(
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
 def reply_to_comment11(self, video_id, comment_id, comment_text):
    try:
        response = self.service1.comments().insert(
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
 def reply_to_comment12(self, video_id, comment_id, comment_text):
    if comment_id is None:
     print (f"No comment to reply to, Comment_id : {comment_id}")
    try:
        response = self.service1.comments().insert(
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
  with open('videos.csv', 'r') as file:
   data = csv.reader(file)
   for row in data:
#     print (row)
     channel_id = row[0]
#     print (channel_id)
     video_id = row[1]
     print (video_id)
     if __name__ == '__main__':
      self.service = self.authenticate()
      self.service1 = self.authenticate1()
      self.service2 = self.authenticate2()
      self.service3 = self.authenticate3()
#      self.service4 = self.authenticate4()
#      self.service5 = self.authenticate5()
#      self.service6 = self.authenticate6()
     comment_text = open("comment.txt").read()
     comment_text1 = open("comment1.txt").read()
     comment_text2 = open("comment2.txt").read()
     comment_text3 = open("comment3.txt").read()
     comment_text4 = open("comment4.txt").read()
     comment_text5 = open("comment5.txt").read()
     comment_text6 = open("comment6.txt").read()
     comment_text7 = open("comment7.txt").read()
     comment_text8 = open("comment8.txt").read()
     comment_text9 = open("comment9.txt").read()
     comment_text10 = open("comment10.txt").read()
     comment_text11 = open("comment11.txt").read()
     comment_text12 = open("comment12.txt").read()
     comment_info = self.post_comment(video_id, comment_text)
     comment_id = comment_info["comment_id"]
     link = self.get_link(video_id, comment_id, channel_id)
     reply_id = self.reply_to_comment(video_id, comment_id, comment_text1)
     reply_id1 = self.reply_to_comment1(video_id, comment_id, comment_text2)
     reply_id2 = self.reply_to_comment2(video_id, comment_id, comment_text3)
     reply_id3 = self.reply_to_comment3(video_id, comment_id, comment_text4)
     reply_id4 = self.reply_to_comment4(video_id, comment_id, comment_text5)
     reply_id5 = self.reply_to_comment5(video_id, comment_id, comment_text6)
     reply_id6 = self.reply_to_comment6(video_id, comment_id, comment_text7)
     reply_id7 = self.reply_to_comment7(video_id, comment_id, comment_text8)
#     reply_id8 = self.reply_to_comment8(video_id, comment_id, comment_text9)
#     reply_id9 = self.reply_to_comment9(video_id, comment_id, comment_text10)
#     reply_id10 = self.reply_to_comment10(video_id, comment_id, comment_text11)
#     reply_id11 = self.reply_to_comment11(video_id, comment_id, comment_text12)
     links = self.get_link(video_id, reply_id, channel_id)
     with open('links', 'a+') as lin:
      lin.write(links+'\n')
      lin.close()
     print(f"\n[-] {links}")
     print(f"\n[=] {reply_id}")
     print(f"\n[+] {comment_info}")
     print(f"\n[-] {link}\n")

my_comment= Youtube_Comment()
my_comment.run()
