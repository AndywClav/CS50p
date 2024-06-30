while True:
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if 
        print(f'{x}:{y}')
    except ValueError:
        print(f'ValueError')
