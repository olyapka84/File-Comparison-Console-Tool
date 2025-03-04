from gendiff.build_diff import generate_diff_tree
from gendiff.formats import format_diff
from gendiff.parse import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1, file2 = parse_file(file_path1), parse_file(file_path2)
    diff = generate_diff_tree(file1, file2)
    return format_diff(diff, format_name)
