from urllib.parse import urlparse, parse_qs

youtube_link = input("Enter the YouTube video link: ")

parsed_url = urlparse(youtube_link)

url_params = parse_qs(parsed_url.query)
video_id = url_params["v"][0]
channel_id = url_params["list"][0]

print("Video ID:", video_id)
print("Channel ID:", channel_id)
