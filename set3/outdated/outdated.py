mouths = [
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
        date = input("Dates: ").title()
        if "/" in date:
            day, mouth, year = date.split("/")
            if day <= 31 or mouth <= 12:
                print(f"{int(year)}-{int(day):02d}-{int(mouth):02d}")
                break
        elif " " in date:
                mouth, day, year = date.split(" ")
                if date.startswith(mouth) and mouth in mouths:
                    if day <= 31 or mouth <= 12:
                        print(f"{int(year)}-{(mouth)}-{int(day):02d}")
                        break
    except:
        break
