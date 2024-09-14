import sys
import os

def main():
    validate_arguments()


def validate_arguments():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]
    new_filename = sys.argv[2]

    if not os.path.splitext(filename)[1] or not os.path.splitext(new_filename)[1]:
        print("Invalid input: Both files must have a valid extension")
        sys.exit(1)

    if os.path.splitext(filename)[1] != os.path.splitext(new_filename)[1]:
        print("Input and output have different extensions")
        sys.exit(1)

    return filename, new_filename


if __name__ == "__main__":
    main()
