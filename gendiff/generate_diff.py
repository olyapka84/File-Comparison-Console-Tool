from gendiff.buid_diff import build_diff
from gendiff.formats.json import format_json
from gendiff.formats.plain import format_plain
from gendiff.formats.stylish import format_stylish
from gendiff.parse import return_dict


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1, file2 = return_dict(file_path1), return_dict(file_path2)
    diff = build_diff(file1, file2)

    if format_name == "stylish":
        return "{\n" + format_stylish(diff) + "\n}"
    if format_name == "plain":
        return format_plain(diff)
    if format_name == "json":
        return format_json(diff)
