import argparse


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

    args = parser.parse_args()

    first_file = args.first_file
    second_file = args.second_file


if __name__ == "__main__":
    main()