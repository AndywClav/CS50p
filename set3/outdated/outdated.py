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
    print(f"{ year }-0{ mouth }-0{ day }")
elif " " in date:
    day, mouth, year = date.split(" ")
