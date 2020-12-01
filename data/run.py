import json
import urllib.request

with urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UUirrYErHzS2TR20MRAK6BWg&key=AIzaSyAzIUs0f4Mm1tqXOxc6EXIUnZLi2Nfgyns") as url:
    data = json.loads(url.read().decode())
	
#solditems = requests.get('https://github.com/timeline.json') # (your url)
#data = solditems.json()
with open('videos.json', 'w') as f:
    json.dump(data, f)
	
	
