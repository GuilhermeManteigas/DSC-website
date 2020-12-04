import json
import urllib.request
import urllib.parse

user_agent = \
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UUirrYErHzS2TR20MRAK6BWg&key=AIzaSyAzIUs0f4Mm1tqXOxc6EXIUnZLi2Nfgyns'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
#data = response.read()
data = json.loads(response.read().decode())

#with urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UUirrYErHzS2TR20MRAK6BWg&key=AIzaSyAzIUs0f4Mm1tqXOxc6EXIUnZLi2Nfgyns") as url:
#	data = json.loads(url.read().decode())
#	print(data)

with open('videos.json', 'w+') as f:
    json.dump(data, f)

#f = open("videos.json", "w+")
#f.write(data)
#f.close()