import json
from math import factorial
from pprint import pprint

path = '/Users/piat/s5/cp2/Mask_RCNN/samples/balloon/dataset/train/via.json'

with open(path, "r") as st_json:

    st_python = json.load(st_json)
file_list = list(st_python.keys())
pprint(file_list[0]+str(st_python[file_list[0]]['size']))

doc = {}
for i in range(len(file_list)):
    region = {}
    for a in range(len(st_python[file_list[i]]['regions'])):
        region[a] = {'shape_attributes' : st_python[file_list[i]]['regions'][a]['shape_attributes'], 'region_attributes' : st_python[file_list[i]]['regions'][a]['region_attributes']}
    doc[file_list[i]+str(st_python[file_list[i]]['size'])] = {"fileref": "", 'size': st_python[file_list[i]]['size'], 'filename':file_list[i],'base64_img_data':"", 'file_attributes': {}, 'regions' : region}

with open('via_region_data.json', 'w') as f:
    json.dump(doc, f)