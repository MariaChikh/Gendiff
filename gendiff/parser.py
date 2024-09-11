import json
import yaml

def parser(file):
    if file.endswith('.json'):
        new_file = json.load(open(file))
    elif file.endswith('.yaml') or file.endswith('.yml'):
        new_file = yaml.safe_load(open(file))
    return new_file