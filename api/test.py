import requests
import json
from controller import *

json1 = {
    "latitude": 55.4507,
    "longitude": 37.3656,
    "limit": 15,
    "offset": 5,
    "usd_available": True,
    "euro_available": True,
}
x = requests.post(url=f"http://{HOST}:{PORT}/api/get_points", json=json1)
print(x.content)
from itertools import accumulate
