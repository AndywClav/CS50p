import sys
import tabulate

def main():
    filename = validate_arguments()
    print(filename)


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


def formate_csv():


if __name__ == "__main__":
    main()
