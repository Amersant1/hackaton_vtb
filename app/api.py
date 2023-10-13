from utils import *
from data_base import *
import json
from controller import *
import os


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
