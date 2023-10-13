"""РАБОТА С МОДЕЛЬЮ ЮЗЕР ИЗ БД"""
from controller import *
from sqlalchemy import desc

from model import *


def make_session():
    session = sessionmaker(engine)()
    return session


def find_nearest_banks(
    latitude: float,
    longitude: float,
    usd_available: bool = None,
    euro_available: bool = None,
    limit: int = 15,
    offset: int = 0,
):  # limit-количество банков, которое вернуть
    _session = make_session()
    filters = list()
    if usd_available:
        filters.append(Bank.usd_available == True)
    if euro_available:
        filters.append(Bank.euro_available == True)
    filters = tuple(filters)
    if filters:
        banks = (
            _session.query(Bank)
            .filter(filters)
            .order_by(
                (Bank.latitude - latitude) * (Bank.latitude - latitude)
                + (Bank.longitude - longitude) * (Bank.longitude - longitude)
            )
            .offset(offset)
            .limit(limit)
        )
    else:
        banks = (
            _session.query(Bank)
            .order_by(
                (Bank.latitude - latitude) * (Bank.latitude - latitude)
                + (Bank.longitude - longitude) * (Bank.longitude - longitude)
            )
            .offset(offset)
            .limit(limit)
        )
    banks = list(banks)
    for i in range(len(banks)):
        banks[i] = banks[i].__dict__
        del banks[i]["_sa_instance_state"]
    _session.close()

    return banks


# find_nearest_banks(55.4507, 37.3656, limit=10,offset=5)
# find_nearest_banks(55.4507, 37.3656, limit=10,offset=0)
