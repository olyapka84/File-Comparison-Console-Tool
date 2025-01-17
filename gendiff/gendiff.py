import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


file1_path = "/Users/olgaakukina/PycharmProjects/python-project-50/test_data/file1.json"
file2_path = "/Users/olgaakukina/PycharmProjects/python-project-50/test_data/file2.json"

file1_data = read_json(file1_path)
file2_data = read_json(file2_path)

print("Data from file1:", file1_data)
print("Data from file2:", file2_data)
