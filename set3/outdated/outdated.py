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
    print(f"{date} with slash")
elif " " in date:
    print(f"{date} with space")
