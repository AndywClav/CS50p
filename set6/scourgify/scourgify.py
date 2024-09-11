import sys
import csv

def main():
    filename, new_filanme = validate_arguments()
    list_filename = file_read(filename)



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


def file_read(filename):
    try:
        with open(filename, "r") as file:
            render = csv.reader(file)
            return list(render)

    except FileNotFoundError:
        print("File does not exist ")
        sys.exit(1)


def file_write(new_filename):
    with open(new_filename, "a") as file:
            render = csv.reader(file)


if __name__ == "__main__":
    main()
