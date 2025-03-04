import argparse


def parse_arguments():
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
        choices=["json", "stylish", "plain"],
        default="stylish",
        metavar="FORMAT",
        help="set format of output (default: stylish)."
    )

    return parser.parse_args()
