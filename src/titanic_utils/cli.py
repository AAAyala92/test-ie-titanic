import sys
import argparse

from titanic_utils.str_utils import extract_titles


def main():
    parser = argparse.ArgumentParser(description="Extract the title from a name")
    parser.add_argument("--name", required=False, help="Name to extract title from")
    parser.add_argument("--names-list", help="List of names separated by ;")
    args = parser.parse_args()

    list_of_names = args.names_list.split(";")
    for name in list_of_names:
        print(extract_titles(name))

    # print(extract_titles(args.name))


if __name__ == "__main__":
    # This part will be executed
    # when calling the script from the terminal
    main()
