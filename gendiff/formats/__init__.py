from gendiff.formats.json import format_json
from gendiff.formats.plain import build_plain_output
from gendiff.formats.stylish import build_stylish_output


def format_diff(diff, format_name):
    if format_name == "stylish":
        return "{\n" + build_stylish_output(diff) + "\n}"
    if format_name == "plain":
        return build_plain_output(diff)
    if format_name == "json":
        return format_json(diff)
    raise ValueError(f"Unsupported format: {format_name}")
