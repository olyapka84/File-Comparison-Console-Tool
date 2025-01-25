import argparse

from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument(
        "first_file",
        type=str,
        help="Path to the first file."
    )
    parser.add_argument(
        "second_file",
        type=str,
        help="Path to the second file."
    )

    parser.add_argument(
        "-f", "--format",
        choices=["json", "plain"],
        default="plain",
        metavar="FORMAT",
        help="set format of output (default: plain)."
    )

    args = parser.parse_args()

    first_file = args.first_file
    second_file = args.second_file

    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == "__main__":
    main()