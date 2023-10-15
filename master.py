import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Check if we have saved credentials
if os.path.exists("token.jsonn"): #	pickle"):
    with open("token.json", "rb") as token:
        creds = token.read()
else:
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open("token.pickle", "wb") as token:
        pickle.dump(creds, token)

# Create the YouTube API service
youtube = build("youtube", "v3", credentials=creds)
# Define the video ID and the comment
video_id = input("YOUR_VIDEO_ID: ")
comment_text = "Your comment here."

# Call the API to add a comment
youtube.commentThreads().insert(
    part="snippet",
    body={
        "snippet": {
            "topLevelComment": {
                "snippet": {
                    "videoId": video_id,
                    "textOriginal": comment_text,
                }
            }
        }
    }
).execute()
# Define the parent comment's ID and the reply text
parent_comment_id = "PARENT_COMMENT_ID"
reply_text = "Your reply here."

# Call the API to add a reply
youtube.comments().insert(
    part="snippet",
    body={
        "snippet": {
            "parentId": parent_comment_id,
            "textOriginal": reply_text,
        }
    }
).execute()

