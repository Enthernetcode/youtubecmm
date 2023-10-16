from urllib.parse import urlparse, parse_qs

youtube_link = input("Enter the YouTube video link: ")

parsed_url = urlparse(youtube_link)

video_id = parsed_url.path.split("/")[-1]

query_params = parse_qs(parsed_url.query)
channel_id = query_params.get("si", [""])[0].split("_")[-1]

print("Video ID:", video_id)
print("Channel ID:", channel_id)
