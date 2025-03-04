from gendiff.formats.json import format_json
from gendiff.formats.plain import format_plain
from gendiff.formats.stylish import format_stylish


def format_diff(diff, format_name):
    if format_name == "stylish":
        return "{\n" + format_stylish(diff) + "\n}"
    if format_name == "plain":
        return format_plain(diff)
    if format_name == "json":
        return format_json(diff)
    raise ValueError(f"Unsupported format: {format_name}")
