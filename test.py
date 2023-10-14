import requests
import json

json1 = {"latitude": 55.4507, "longitude": 37.3656, "limit": 1, "offset": 5,"usd_available":True,
"euro_available":True}
x = requests.post(url="http://localhost:9002/api/update_number_of_people_info", json=json.dumps(json1))
print(x.content)
