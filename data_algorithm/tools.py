import json


def convert(json_str):
    data = json.loads(json_str)
    names = [d['name'] for d in data]
    return names


def convert_cast(json_str):
    data = json.loads(json_str)
    counter = 0
    names = []
    for d in data:
        if counter < 3:
            names.append(d['name'])
        counter += 1
    return names


def fetch_director(json_str):
    data = json.loads(json_str)
    names = []
    for d in data:
        if d["job"] == "Director":
            names.append(d['name'])
    return names


def collapse(objects):
    new_objects = [obj.replace(" ", "")for obj in objects]
    return new_objects
