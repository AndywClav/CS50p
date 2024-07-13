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

try:
    date = input().strip().title()
    if date in mouths:
        print()
except:
    pass
else:
    print("SI")
