from controller import *
from model import *
import json
from data_base import *
from random import *

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

def get_info_about_number_of_people_came():
    _session=make_session()
    banks=_session.query(Bank).filter(Bank.type=="office").all()
    list_of_banks=dict()
    
    for bank in banks:
        dictionary=dict()
        #первое значение-время ожидания,2-значение колитчество за прошедний годб 3- вероятность события, 
        number_of_clients=randint(10000,100000)
        n=0
        rand=randint(0,number_of_clients-n)
        dictionary["number_of_clients"]=number_of_clients
        make_card=[randint(5,10),rand,rand/number_of_clients,]
        n+=rand
        rand=randint(0,number_of_clients-n)
        dictionary["make_card"]=make_card

        mortgage=[randint(60,90),rand,rand/number_of_clients]
        n+=rand
        rand=randint(0,number_of_clients-n)
        dictionary["mortgage"]=mortgage


        insurance=[randint(30,40),rand,rand/number_of_clients]
        dictionary["insurance"]=insurance
        n+=rand
        rand=randint(0,number_of_clients-n)
        
        credit=[randint(30,60),rand,rand/number_of_clients]
        dictionary["credit"]=credit
        n+=rand
        rand=randint(0,number_of_clients-n)

        poshlina=[randint(15,30),rand,rand/number_of_clients]
        dictionary["poshlina"]=poshlina
        n+=rand
        rand=randint(0,number_of_clients-n)

        payments=[randint(10,15),rand,rand/number_of_clients]
        dictionary["payments"]=payments
        n+=rand
        rand=randint(0,number_of_clients-n)

        deposit=[randint(20,40),rand,rand/number_of_clients]
        dictionary["deposit"]=deposit
        n+=rand
        rand=randint(0,number_of_clients-n)
        
        check_info=[randint(10,15),rand,rand/number_of_clients]
        dictionary["check_info"]=check_info
        rand=randint(0,number_of_clients-n)
        n+=rand

        government_pay=[randint(20,25),rand,rand/number_of_clients]
        dictionary["government_pay"]=government_pay
        rand=randint(0,number_of_clients-n)
        n+=rand
        
        math_expectation=int()
        for key in dictionary.keys():
            list1=dictionary[key]
            if key!="number_of_clients":
                math_expectation+=list1[2]*list1[0]
        if math_expectation>20:
            math_expectation=20
        dictionary["math_expectation"]=math_expectation
        list_of_banks[bank.id]=dictionary
    
    with open("math_expectation.json","w") as file:
        print(json.dumps(list_of_banks),file=file)
    

        
get_info_about_number_of_people_came()