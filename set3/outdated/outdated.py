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
            print(f"{int(year)}-{int(mouth):02d}-{int(day):02d}")
            break
        elif " " in date:
                mouth, day, year = date.split(" ")
                if date.startswith(mouth) and mouth in mouths:
                    print(f"{int(year)}-{(mouth)}-{int(day):02d}")
                    break
    except:
        break
