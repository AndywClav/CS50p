while True:
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        print(f'{x}:{y}')
    except ValueError:
        print(f'ValueError')
