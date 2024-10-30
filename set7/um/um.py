import re
import sys


def main():
    output = input_aa()
    print(count(output))


def count(s):
    ...

def input_aa():
    if sys.argv[1:]:
        input_string = sys.argv[1:]
            return input_string

    return input("Text: ")


if __name__ == "__main__":
    main()
