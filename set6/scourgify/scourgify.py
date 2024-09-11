import sys
import csv

def main():
    validate_arguments()


def validate_arguments():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    print(sys.argv)
    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        print("Not a Csv file")
        sys.exit(1)

    return filename


def file_read(filename):
    try:
        with open(filename, "r") as file:
            render = csv.reader(file)
            return list(render)

    except FileNotFoundError:
        print("File does not exist ")
        sys.exit(1)


if __name__ == "__main__":
    main()
