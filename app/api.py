from utils import *
from data_base import *
import json
from controller import *
import os


number_of_people_in_bank=dict()

def dir_last_updated(folder):
    return str(
        max(
            os.path.getmtime(os.path.join(root_path, f))
            for root_path, dirs, files in os.walk(folder)
            for f in files
        )
    )


@app.route("/test")
def testing_route():
    return json.dumps("WORKS")

@app.route("/update_number_of_people_info")
def update_people_info():
    global number_of_people_in_bank
    data = json.loads(request.get_json())
    id=data["id"]
    total=data["total"]
    number_of_people_in_bank[id]=total


@app.route("/get_points", methods=["POST", "GET"])
def get_best_points():
    data = json.loads(request.get_json())
    if "usd_available" in data:
        usd_available = True
    else:
        usd_available = None
    if "euro_available" in data:
        euro_available = True
    else:
        euro_available = None
    latitude = data["latitude"]
    longitude = data["longitude"]
    if "offset" in data:
        offset = data["offset"]
    else:
        offset = 0
    if "limit" in data:
        limit = data["limit"]
    else:
        limit = 15
    banks = find_nearest_banks(
        latitude=latitude,
        longitude=longitude,
        offset=offset,
        limit=limit,
        euro_available=euro_available,
        usd_available=usd_available,
    )
    
    for bank in banks:
        bank["number_of_people"]=number_of_people_in_bank[bank["id"]]


    return json.dumps(banks)
