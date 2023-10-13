from typing import Any
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import relation
from sqlalchemy.orm import sessionmaker,relationship
from posixpath import abspath
from os.path import join
import sys
sys.path.append("../")
from controller import engine, Base, Session
from datetime import datetime


# class User(Base):
#     """_summary_

#     Args:
#         Base (_type_): _description_
#     """
#     __tablename__="user"
#     pass

# class Bank(Base):
#     """_summary_

#     Args:
#         Base (_type_): _description_
#     """
#     pass