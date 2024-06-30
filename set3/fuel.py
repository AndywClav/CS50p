while True:
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        resul = x / y
        return resul
    except ValueError:
        print(f'ValueError')
    except ZeroDivisionError:
        print(f'ZeroDivisionError')
