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

date = input().strip().title()

if "/" in date:
    day, mouth, year = date.split("/")
    print(f"{int(year)}-{int(mouth):02d}-{int(day):02d}")
elif " " in date:
    day, mouth, year = date.split(" ")
