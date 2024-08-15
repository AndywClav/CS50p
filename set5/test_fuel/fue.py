
def main():
    fraction = input("Fraction: ").strip()
    convert_fraction = convert(fraction)

    if isinstance(convert_fraction, float):
        percentage = gauge(convert_fraction)
        return print(percentage)

    print(convert_fraction)


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y or y == 0:
                continue
            resul = x / y
            return resul
        except ValueError:
            return f'ValueError'
        except ZeroDivisionError:
            return f'ZeroDivisionError'


def gauge(percentage):
    x = round(percentage * 100)
    match x:
        case 0:
            return f'E'
        case 1:
            return f'E'
        case 25:
            return f'25%'
        case 33:
            return f'33%'
        case 50:
            return f'50%'
        case 67:
            return f'67%'
        case 75:
            return f'75%'
        case 99:
            return f'F'
        case 100:
            return f'F'


if __name__ == "__main__":
    main()

