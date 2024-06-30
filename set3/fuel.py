while True:
    try:
        fraction = input("Fraction: ").strip()
        int(x), int(y) = fraction.split("/")
        print(f'{x}:{y}')
    except ValueError:
        print(f'ValueError')
