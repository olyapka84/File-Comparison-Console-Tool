import os

from gendiff.build_diff import generate_diff_tree
from gendiff.formats import format_diff
from gendiff.parser import parse


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]


def get_file_data(file_path):
    with open(file_path) as file:
        return parse(file, get_extension(file_path))


def generate_diff(file1_path, file2_path, style='stylish'):
    data1 = get_file_data(file1_path)
    data2 = get_file_data(file2_path)
    diff_tree = generate_diff_tree(data1, data2)
    formatted_diff = format_diff(diff_tree, style)
    return formatted_diff
