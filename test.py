import requests
import json

json1 = {
    "latitude": 55.4507,
    "longitude": 37.3656,
    "limit": 1,
    "offset": 5,
    # "usd_available": True,
    # "euro_available": True,
}
x = requests.post(url="http://192.168.88.217:5000/api/get_points", json=json.dumps(json1))
print(x.content)
