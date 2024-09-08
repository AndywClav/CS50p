import sys

def main():
    filename = validate_arguments()
    total_lines = count_lines(filename)
    print(total_lines)


def count_lines(filename):
    try:
        with open(filename, "r") as file:
            line_file = file.readlines()

            code_lines = [
                line for line in line_file
                if line.strip() != "" and not line.strip().startswith("#")
            ]
            return len(code_lines)
    except FileNotFoundError:
        print("File does not exist ")
        sys.exit


def validate_arguments():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    return filename


if __name__ == "__main__":
    main()
