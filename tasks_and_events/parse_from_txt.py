from controller import *
from model import *
import json
from data_base import *

if __name__ == "__main__":
    _session = make_session()
    typical_working_hours = [
        {"days": "пн", "hours": "09:00-18:00"},
        {"days": "вт", "hours": "09:00-18:00"},
        {"days": "ср", "hours": "09:00-18:00"},
        {"days": "чт", "hours": "09:00-18:00"},
        {"days": "пт", "hours": "09:00-18:00"},
        {"days": "сб", "hours": "09:00-18:00"},
        {"days": "вс", "hours": "09:00-18:00"},
    ]
    support_usd = True
    support_euro = True
    usd_available = True
    euro_available = True
    with open("hackaton_vtb/offices.txt", "r", encoding="utf-8") as file:
        full_list = json.loads(file.read())
        for elem in full_list:
            bank1 = Bank(
                latitude=elem["latitude"],
                longitude=elem["longitude"],
                address=elem["address"],
                type="office",
                name=elem["salePointName"],
                open_hours=json.dumps(elem["openHours"]),
                metro_station=elem["metroStation"],
                number_of_people=0,
                support_usd=support_usd,
                support_euro=support_euro,
                usd_available=usd_available,
                euro_available=euro_available,
            )
            _session.add(bank1)
    with open("hackaton_vtb/atms.txt", "r", encoding="utf-8") as file:
        full_list = json.loads(file.read())["atms"]
        for elem in full_list:
            service = elem["services"]

            if service["supportsUsd"]["serviceCapability"] == "SUPPORTED":
                support_usd = True
            else:
                support_usd = False

            if service["supportsEur"]["serviceCapability"] == "SUPPORTED":
                support_euro = True
            else:
                support_euro = False

            if service["supportsEur"]["serviceActivity"] == "AVAILABLE":
                euro_available = True
            else:
                euro_available = False

            if service["supportsUsd"]["serviceActivity"] == "AVAILABLE":
                usd_available = True
            else:
                usd_available = False

            if elem["address"] == str():
                name = "банкомат"
            else:
                name = "банкомат по адресу: " + elem["address"]

            if elem["allDay"] == False:
                open_hours = typical_working_hours
            else:
                open_hours = "all day"

            bank1 = Bank(
                latitude=elem["latitude"],
                longitude=elem["longitude"],
                address=elem["address"],
                type="atm",
                name=name,
                open_hours=open_hours,
                metro_station=None,
                support_usd=support_usd,
                support_euro=support_euro,
                usd_available=usd_available,
                euro_available=euro_available,
            )
            _session.add(bank1)
    _session.commit()
    _session.close()
