from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

API_KEY = 'YOUR_API_KEY_HERE'

def get_authenticated_service():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/youtube.force-ssl'])
    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, ['https://www.googleapis.com/auth/youtube.force-ssl'])
        credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as tokenfile:
            tokenfile.write(credentials.to_json())
    service = build('youtube', 'v3', developerKey=API_KEY, credentials=credentials)
    return service

def post_comment(video_id, comment_text):
    try:
        youtube = get_authenticated_service()
        insert_result = youtube.commentThreads().insert(
            part="snippet",
            body=dict(snippet=dict(channelId=CHANNEL_ID,videoId=video_id,topLevelComment=dict(snippet=dict(textOriginal=comment_text))))).execute()
        comment = insert_result["snippet"]["topLevelComment"]
        print(f'Comment "{comment["snippet"]["textOriginal"]}" was posted on {video_id}.')
    except HttpError as error:
        print(f'An error occurred: {error}')

post_comment('VIDEO_ID_HERE', 'YOUR_COMMENT_HERE')
