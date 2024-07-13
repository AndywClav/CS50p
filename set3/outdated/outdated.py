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
convert_slash = date.split("/")
convert_space = date.split(" ")
if convert_slash:
    print(f"{date} with slash")
elif convert_space:
    print(f"{date} with space")
