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
    print(f"{ year }-{ mouth:.2f }-{ day:.2f }")
elif " " in date:
    day, mouth, year = date.split(" ")
