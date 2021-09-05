
import json

def generate_text():
    mc = load_mc()

def load_mc():
    mc = {}
    with open('mc.json', 'r') as mcjson:
        mc = json.loads(mcjson)
    return mc
