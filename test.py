import requests
import json

json1 = {"latitude": 55.4507, "longitude": 37.3656, "limit": 10, "offset": 5}
x = requests.post(url="http://192.168.88.217:5000/get_points", json=json.dumps(json1))
print(x.content)
