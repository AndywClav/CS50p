import sys

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

    return filename, new_filename


if __name__ == "__main__":
    main()
