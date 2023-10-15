"""РАБОТА С МОДЕЛЬЮ Bank ИЗ БД"""
from controller import *
from sqlalchemy import desc

from model import *


def make_session():
    session = sessionmaker(engine)()
    return session


def find_nearest_banks(
    latitude: float,#широта
    longitude: float,#долгота 
    type: str = None,# tms/office
    usd_available: bool = None,#доступны ли доллары
    euro_available: bool = None,#доступны ли евро
    limit: int = 15,
    offset: int = 0,
):  # limit-количество банков, которое вернуть
    _session = make_session()
    filters = list()
    bank = select(Bank)

    if usd_available != None:
        bank = bank.where(Bank.usd_available == True)

    if euro_available != None:
        bank = bank.where(Bank.euro_available == True)

    if type != None:
        bank = bank.where(Bank.type == type.lower)

    bank = (
        bank.order_by(
            (Bank.latitude - latitude) * (Bank.latitude - latitude)
            + (Bank.longitude - longitude) * (Bank.longitude - longitude)
        )  # сортируем по расстоянию от юзера до отделения/банкомата
        .offset(offset)
        .limit(limit)
    )

    banks = _session.scalars(bank)

    banks = list(banks)
    for i in range(len(banks)):
        banks[i] = banks[i].__dict__  # превращаем объект в словарь и удаляем ненужный ключ
        del banks[i]["_sa_instance_state"]
    _session.close()

    return banks


# find_nearest_banks(55.4507, 37.3656, limit=10,offset=5)
# find_nearest_banks(55.4507, 37.3656, limit=10,offset=0)
