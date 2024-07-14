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
        date = input().strip().title()
        if "/" in date:
            day, mouth, year = date.split("/")
            print(f"{int(year)}-{int(mouth):02d}-{int(day):02d}")
    except:
        pass
