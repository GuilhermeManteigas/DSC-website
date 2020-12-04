import json
import urllib.request
import requests

link = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UUirrYErHzS2TR20MRAK6BWg&key=AIzaSyAzIUs0f4Mm1tqXOxc6EXIUnZLi2Nfgyns"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

json = requests.get(link, headers=headers).text


with open('videos.json', 'w+') as f:
    f.write(json)