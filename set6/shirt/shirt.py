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

    if not filename.endswith(".csv") and new_filename:
        print("Not a Csv file")
        sys.exit(1)

    return filename, new_filename


if __main__ == "__main__":
    main()
