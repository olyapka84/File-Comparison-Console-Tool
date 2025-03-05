import json

import yaml


def parse_file(file_path):
    if not (file_path.endswith(".json") or file_path.endswith(".yaml")
            or file_path.endswith(".yml")):
        raise ValueError(f"Unsupported file format: {file_path}")
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        if file_path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(file)
