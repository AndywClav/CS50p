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
        start_mouth = date.startswith(mouths)
        if "/" in date:
            day, mouth, year = date.split("/")
            print(f"{int(year)}-{int(mouth):02d}-{int(day):02d}")
        elif start_mouth:
            mouth, day, year = date.split("/")
            print(mouth)
    except:
        pass
