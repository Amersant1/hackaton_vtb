from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, request, render_template, abort
from flask_cors import CORS
import sys


# database = 'horoscope'
Base = declarative_base()
user = "hackaton_user"
password = "Sergey123()"
host = "185.209.29.236"
port = 3306

database = "hackaton"
connection_string = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
)


engine = create_engine(url=connection_string)

Session = sessionmaker(engine)()


app = Flask(__name__, static_folder="static")
CORS(app)
if sys.platform == "win32":
    HOST = "0.0.0.0"
    PORT = 5000
else:
    HOST = "185.209.29.236"
    PORT = "5000"
