while True:
    fraction = input("Fraction: ").strip()
    x, y = fraction.split("/")
    if int(x) == True and int(y) == True:
        print(type(x), type(y))
        continue
