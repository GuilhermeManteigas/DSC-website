import json
import requests

solditems = requests.get('https://github.com/timeline.json') # (your url)
data = solditems.json()
with open('data.json', 'w') as f:
    json.dump(data, f)