months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Dates: ").strip().title()
        if "/" in date:
            parts = date.split("/")
            if len(parts) == 3:
                month, day, year = parts
                day = day.replace(",", "").strip()
                if day.isdigit() and month.isdigit() and year.isdigit() and int(day) <= 31 and 1 <= int(month) <= 12:
                    print(f"{int(year)}-{int(month):02d}-{int(day):02d}")
                    break
                else:
                    print("Invalid date format, please try again.")
            else:
                print("Invalid date format, please try again.")
        elif "," in date:
            parts = date.split(" ")
            if len(parts) == 3:
                month, day, year = parts
                day = day.replace(",", "").strip()
                if month in months and day.isdigit() and year.isdigit() and int(day) <= 31:
                    month_index = months.index(month) + 1
                    print(f"{int(year)}-{month_index:02d}-{int(day):02d}")
                    break
                else:
                    print("Invalid date format, please try again.")
            else:
                print("Invalid date format, please try again.")
        else:
            print("Invalid date format, please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
