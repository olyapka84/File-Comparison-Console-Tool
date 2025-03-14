#!/usr/bin/env python3
from gendiff.cli import parse_arguments
from gendiff.generated_diff import generate_diff


def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
