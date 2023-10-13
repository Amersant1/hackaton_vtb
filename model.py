from typing import Any
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy import relation
from sqlalchemy.orm import sessionmaker, relationship
from posixpath import abspath
from os.path import join
import sys

sys.path.append("../")
from controller import engine, Base, Session
from datetime import datetime



class Bank(Base):
    """
    id - int
    latitude-Float (широта)
    longitude - Float(долгота)
    address- string (адрес)
    type-string (office/tms)
    name-string (название)
    open_hours-json
    metro_station-str
    number_of_people-int количество человек в отделении
    support_usd - bool (поддерживает ли выдачу в долларах)
    support_euro - bool (поддерживает ли выдачу в евро)
    usd_available - bool (доступны ли сейчас доллары )
    euro_available - (доступны ли евро)
    """

    __tablename__ = "banks"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    latitude = Column(Float(50))
    longitude = Column(Float(50))
    address = Column(String(400))
    type = Column(String(30))  # банкомат или офис
    name = Column(String(500))
    open_hours = Column(JSON)  # in json
    metro_station = Column(String(100))
    number_of_people = Column(Integer)
    support_usd = Column(Boolean)
    support_euro = Column(Boolean)
    usd_available = Column(Boolean)
    euro_available = Column(Boolean)


# Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)
# Base.metadata.drop(engine)
