import json

import yaml


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
