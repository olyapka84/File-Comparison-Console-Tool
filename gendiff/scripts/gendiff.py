from gendiff.cli import parse_arguments
from gendiff.build_diff import generate_diff_tree
from gendiff.parse import parse_file
from gendiff.formats import format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1, file2 = parse_file(file_path1), parse_file(file_path2)
    diff = generate_diff_tree(file1, file2)
    return format_diff(diff, format_name)


def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
