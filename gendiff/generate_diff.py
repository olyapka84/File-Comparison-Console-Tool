from gendiff.parse import read_json, read_yaml


def generate_diff(file_path1, file_path2):
    if file_path1.endswith('.json'):
        file1, file2 = read_json(file_path1), read_json(file_path2)
    else:
        file1, file2 = read_yaml(file_path1), read_yaml(file_path2)
    added = {key: file2[key] for key in file2.keys() - file1.keys()}
    removed = {key: file1[key] for key in file1.keys() - file2.keys()}
    modified = {key: (file1[key], file2[key]) for key in file1.keys() & file2.keys() if file1[key] != file2[key]}
    unchanged = {key: file1[key] for key in file1.keys() & file2.keys() if file1[key] == file2[key]}

    all_keys = sorted(set(added.keys()) | set(removed.keys()) | set(modified.keys()) | set(unchanged.keys()))

    diff = []
    for key in all_keys:
        if key in removed:
            diff.append(f"- {key}: {removed[key]}")
        if key in added:
            diff.append(f"+ {key}: {added[key]}")
        if key in modified:
            diff.append(f"- {key}: {modified[key][0]}")
            diff.append(f"+ {key}: {modified[key][1]}")
        if key in unchanged:
            diff.append(f"  {key}: {unchanged[key]}")

    formatted_diff = "{\n" + "\n".join(f"  {line}" for line in diff) + "\n}"
    return formatted_diff

# print(generate_diff("/Users/olgaakukina/PycharmProjects/python-project-50/tests/test_data/file1.yaml",
# "/Users/olgaakukina/PycharmProjects/python-project-50/tests/test_data/file2.yaml"))

# print(generate_diff("/Users/olgaakukina/PycharmProjects/python-project-50/tests/test_data/file1.json",
# "/Users/olgaakukina/PycharmProjects/python-project-50/tests/test_data/file2.json"))
