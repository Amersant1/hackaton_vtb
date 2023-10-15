from controller import *
from app import *
from model import *
from data_base import *
from utils import *
# from tasks_and_events import *

# app.run(debug=True, ssl_context=context)


if __name__ == "__main__":
    app.run(host=HOST, debug=True, port=PORT)
