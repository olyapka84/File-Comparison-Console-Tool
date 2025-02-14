import json


def format_json(diff):
    result = {}
    for item in diff:
        result[item["key"]] = item
    return json.dumps(result, indent=4)
