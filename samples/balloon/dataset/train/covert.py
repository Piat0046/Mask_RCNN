import json
from math import factorial
from pprint import pprint

path = '/Users/piat/s5/cp2/Mask_RCNN/samples/balloon/dataset/val/via_region_data.json'

with open(path, "r") as st_json:

    st_python = json.load(st_json)

pprint(st_python)


# pprint(a.keys())