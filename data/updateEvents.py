import json
import urllib.request
import urllib.parse

user_agent = \
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://graph.facebook.com/629732060983637/events?fields=id,name,description,start_time,cover&access_token=EAAGQwBPLbFMBACeZAT5j0ZArkLENhADw6GR5gbcXEa1JpP9CtA0by5xjPZCD9OmeEE4VLxebuiL3nchLlXisRZCjXC8SlK5o8MKbgFyUj36ea34So2ZAHtK2Ic9aXC3UGlKomRLgU5eglm9BxwyDkkvDYSggdG5I9dwIm601ZBu7bnDk7FLoefvORNI0HdZBJgZD'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
data = json.loads(response.read().decode())

with open('events.json', 'w+') as f:
    json.dump(data, f)
