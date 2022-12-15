import json
from constants import CONFIG_FILEPATH

file = open(CONFIG_FILEPATH, "r")
config = json.loads(file.read())

def get_config():
    return config