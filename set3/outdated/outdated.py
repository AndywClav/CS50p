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
                              print(f"{int(year)}-01-{int(day):02d}")
                         case "February":
                              print(f"{int(year)}-02-{int(day):02d}")
                         case "March":
                              print(f"{int(year)}-03-{int(day):02d}")
                         case "April":
                              print(f"{int(year)}-04-{int(day):02d}")
                         case "May":
                              print(f"{int(year)}-05-{int(day):02d}")
                         case "June":
                              print(f"{int(year)}-06-{int(day):02d}")
                         case "July":
                              print(f"{int(year)}-07-{int(day):02d}")
                         case "August":
                              print(f"{int(year)}-08-{int(day):02d}")
                         case "September":
                              print(f"{int(year)}-09-{int(day):02d}")
                         case "October":
                              print(f"{int(year)}-10-{int(day):02d}")
                         case "November":
                              print(f"{int(year)}-11-{int(day):02d}")
                         case "December":
                              print(f"{int(year)}-12-{int(day):02d}")
                    break
    except:
        break
