import json
import yaml


def parser(file):
    if file.endswith('.json'):
        with open(file) as new_file:
            return json.load(new_file)
    elif file.endswith('.yaml') or file.endswith('.yml'):
        with open(file) as new_file:
            return yaml.safe_load(new_file)
