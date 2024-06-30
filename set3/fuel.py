while True:
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        print(f'{x}:{y}')
    except ValueError:
        print(f'{x}:{y}')
