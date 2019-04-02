import requests, json
#
body = json.dumps({u"name": u"feed the api"})
url = u"http://localhost:8080/todos/"
#
r = requests.post(url=url, data=body)
r.content
print(r.content)