from datetime import date

class Date:
    def __init__(self, value_date):
        if "-" in value_date:
            year, month, day = value_date.split("-")
        elif "," in value_date:
            year, month, day = value_date.split(",")
        else:
            raise ValueError("Invalid date format. Use either 'YYYY-MM-DD' or 'YYYY,MM,DD'")

        try:
            date(int(year), int(month), int(day))
        except ValueError:
            raise ValueError("Invalid date")


def get_date():
    return Date(input("Date of Birth: "))


def main():
    print(get_date())


if __name__ == "__main__":
    main()
