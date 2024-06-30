while True:
    try:
        fraction = int(input("Fraction: ")).strip()
        x, y = fraction.split("/")
        print(f'{x}:{y}')
    except ValueError:
        print(f'ValueError')
