import requests, json
#
body = json.dumps({u"handler": u"mqtt"})
url = u"http://192.168.120.33:8123/api/config/config_entries/flow"
headers = {'content-type': 'application/json','authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIwYzc1MmQ3MDUzYTk0MTZiOTJiNjRiMzExZWRhOGFiNSIsImlhdCI6MTU1NDE3NjM1NywiZXhwIjoxNTU0MTc4MTU3fQ.TlapwdbjSQqjUVYFHZfDT0tUdkutWSLlLqV8hOQh4cM'}
#
r = requests.post(url=url, data=body,headers=headers)
r.content
print(r.content)