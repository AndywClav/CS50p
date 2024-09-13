import sys
import csv


def main():
    filename, new_filanme = validate_arguments()
    list_filename = file_read(filename)
    format_filename = format_names(list_filename)
    file_write(new_filanme, format_filename)


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


def format_names(filename):
    formatted_list = []

    formatted_list.append(["first", "last", "house"])

    for row in filename:
        name = row[0]
        house = row[1]

        if ", " in name:
            last_name, first_name = name.split(", ")
        else:
            print(f"Error in format: {name}")
            continue

        formatted_list.append([first_name, last_name, house])

    return formatted_list


def file_write(new_filename, filename):
    with open(new_filename, "a",  newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows(filename)


if __name__ == "__main__":
    main()
