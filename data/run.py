import json
import urllib.request
import urllib.parse

url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UUirrYErHzS2TR20MRAK6BWg&key=AIzaSyAzIUs0f4Mm1tqXOxc6EXIUnZLi2Nfgyns'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   data = json.loads(response.read().decode())

#with urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UUirrYErHzS2TR20MRAK6BWg&key=AIzaSyAzIUs0f4Mm1tqXOxc6EXIUnZLi2Nfgyns") as url:
#	data = json.loads(url.read().decode())
#	print(data)

with open('videos.json', 'w+') as f:
    json.dump(data, f)

#f = open("videos.json", "w+")
#f.write(data)
#f.close()