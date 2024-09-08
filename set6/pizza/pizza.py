import sys
import tabulate

def main():
    filename = validate_arguments()
    table_csv = format_file_read(filename)
    print(tabulate(table_csv, tablefmt="grid"))


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


def format_file_read(filename):
    try:
        with open(filename, "r") as file:
            csv = file.read()
            return csv
    except FileNotFoundError:
        print("File does not exist ")
        sys.exit


if __name__ == "__main__":
    main()
