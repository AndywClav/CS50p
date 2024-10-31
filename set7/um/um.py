import re
import sys

def main():
    output = input_string()
    print(count(output))


def count(s):
    """
    This function counts occurrences of the word "um"
    in a given string, ignoring case sensitivity.
    """
    count_um: int = 0
    um = re.findall(r"\bum\b", s, re.IGNORECASE)
    count_um = len(um)
    return count_um


def input_string():
    """
    This function handles user input, allowing for input either through
    a function call "Input()" or directly from the terminal.
    """
    if sys.argv[1:]:
        input_text = sys.argv[1:]
        return f"{" ".join(input_text)}"

    return input("Text: ")


if __name__ == "__main__":
    main()
