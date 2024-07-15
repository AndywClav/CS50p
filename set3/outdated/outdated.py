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
            mouth, day, year = date.split("/")
            print(f"{int(year)}-{int(mouth):02d}-{int(day):02d}")
            break
        elif " " in date:
                mouth, day, year = date.split(" ")
                if date.startswith(mouth) and mouth in mouths:
                    match mouth:
                         case "January":
                         case "February":
                         case "March",
                         case "April",
                         case "May",
                         case "June",
                         case "July",
                         case "August",
                         case "September",
                         case "October",
                         case "November",
                         case "December"
                    print(f"{int(year)}-{(mouth)}-{int(day):02d}")
                    break
    except:
        break
