import json
from math import factorial
from pprint import pprint

path = '/Users/piat/s5/cp2/Mask_RCNN/samples/balloon/dataset/val/via.json'

with open(path, "r") as st_json:
    st_python = json.load(st_json)

file_list = list(st_python.keys())

doc = {}
for i in range(len(file_list)):
    region = {}
    for a in range(len(st_python[file_list[i]]['regions'])):
        att = st_python[file_list[i]]['regions'][a]['shape_attributes']
        if att['name'] == 'rect':
            region[a] = {'shape_attributes' : {'name' : 'polygon', 'all_points_x' : [att['x'], att['x'], att['x']+att["width"],att['x']+att["width"],att['x']], 'all_points_y' : [att['y'], att['y']+att['height'], att['y']+att['height'],att['y'], att['y']], 'region_attributes' : st_python[file_list[i]]['regions'][a]['region_attributes']}}
        elif att['name'] == 'polygon':
            region[a] = {'shape_attributes' : att, 'region_attributes' : st_python[file_list[i]]['regions'][a]['region_attributes']}
    doc[file_list[i]] = {"fileref": "", 'size': st_python[file_list[i]]['size'], 'filename':st_python[file_list[i]]['filename'],'base64_img_data':"", 'file_attributes': {}, 'regions' : region}

with open('/Users/piat/s5/cp2/Mask_RCNN/samples/balloon/dataset/val/via_region_data.json', 'w') as f:
    json.dump(doc, f)