while True:
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        if int(x) == True and int(y) == True:
            print(f'{x}:{y}')
    except ValueError:
        print(f'ValueError')
