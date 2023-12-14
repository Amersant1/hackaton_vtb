from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, request, render_template, abort
from flask_cors import CORS, cross_origin
import sys


# database = 'horoscope'
Base = declarative_base()
user = str()
password = str()
host = str()
port = int()

database = str()
connection_string = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
)


engine = create_engine(url=connection_string)

Session = sessionmaker(engine)()


app = Flask(__name__, static_folder="static")
CORS(app, resources={r"/api/*": {"origins": "*"}})

if sys.platform == "win32":
    HOST = "localhost"
    PORT = 5000
else:
    HOST = "localhost"
    PORT = 9002
