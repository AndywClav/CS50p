import sys
import tabulate

def main():
    filename = validate_arguments()
    table_csv = format_csv(filename)
    print(table_csv)


def validate_arguments():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        print("Not a Csv file")
        sys.exit(1)

    return filename


def format_csv(filename):
    try:
        with open(filename, "r") as file:
            file.
            return file
    except FileNotFoundError:
        print("File does not exist ")
        sys.exit


if __name__ == "__main__":
    main()
