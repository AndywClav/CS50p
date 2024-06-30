while True:
    fraction = input("Fraction: ").strip()
    x, y = fraction.split("/")
    print(x, y)
    if int(x) == True and int(y) == True:
        print(type(x), type(y))
        return x, y
    else:
