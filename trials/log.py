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

tokens = ["token.json","token1.json","token2.json","token3.json","token4.json","token5.json"]
#for token in tokens:
# print ("{}".format(token))

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
api_key = "AIzaSyAvIKUv_1iuLutcUZfmJJggavgBPKHDTEk"
youtube = build('youtube', 'v3', developerKey=api_key)
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def log():
   creds = None
   for token in tokens:
    print (token)
    if os.path.exists(token): #.json'):
       print (token)
       creds = Credentials.from_authorized_user_file(token, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token, 'w') as token:
            token.write(creds.to_json())
   #return 
   k = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
   print (k)
log()
