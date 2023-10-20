from urllib.parse import urlparse, parse_qs
list = []
links = [
'https://youtu.be/75KjLd5XVMY?si=FwQfjZ9bLYAjhfnm',
'https://youtu.be/75KjLd5XVMY?si=V1ZVS0ZFVPecRbmd'
]
for line in links:
  print(line)
  youtube_link = line
  parsed_url = urlparse(youtube_link)
  video_id = parsed_url.path.split("/")[-1]
  query_params = parse_qs(parsed_url.query)
  channel_id = query_params.get("si", [""])[0].split("_")[-1]
  print("Video ID:", video_id)
  print("Channel ID:", channel_id)
  id = f'{channel_id}, {video_id}'
  list.append(id)
print (list)
for line in list:
 with open('videos.csv', 'a+') as l:
   l.write(line)
   l.write("\n")
   l.close()
   print (line)
