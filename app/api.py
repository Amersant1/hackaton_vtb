from utils import *
# import utils.utils
from data_base import *
# import data_base.bank, data_base.user
import json
from controller import *
import os

banks_info=dict()


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


@app.route("/api/update_number_of_people_info", methods=["POST", "GET"])
def update_people_info():
    
    data = json.loads(request.get_json())
    id = data["id"]
    print(data)
    number_of_people=data["number_of_people"]
    number_of_staff=data["number_of_staff"]
    number_of_salers=data["number_of_salers"]
    math_expectation=data["math_expectation"]
    if id in banks_info:
        
        banks_info[id].update_info(number_of_people=number_of_people,number_of_staff=number_of_staff,number_of_salers=number_of_salers,math_expectation=math_expectation)
        
    else:
        banks_info[id]=BankInfo(id=id,number_of_people=number_of_people,number_of_staff=number_of_staff,number_of_salers=number_of_salers,math_expectation=math_expectation)

    # print(number_of_people_in_bank)
    return json.dumps(True)


@app.route("/api/get_points", methods=["POST", "GET"])
@cross_origin()
def get_best_points():
    global banks_info
    data = json.loads(request.get_json())
    print(data)
    if "usd_available" in data:
        usd_available = True
    else:
        usd_available = None
    if "euro_available" in data:
        euro_available = True
    else:
        euro_available = None
    if "offset" in data:
        offset = data["offset"]
    else:
        offset = 0
    if "limit" in data:
        limit = data["limit"]
    else:
        limit = 15
    latitude = data["latitude"]
    longitude = data["longitude"]
    banks = find_nearest_banks(
        latitude=latitude,
        longitude=longitude,
        offset=offset,
        limit=limit,
        euro_available=euro_available,
        usd_available=usd_available,
    )

    for bank in banks:
        try:
            bank["waiting_time"]=banks_info[bank["id"]].waiting_time
        except Exception as err:
            print(err)
            bank["waiting_time"]=0
    print(bank)
    return json.dumps(banks)
