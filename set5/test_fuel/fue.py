
def main():
    while True:
        fraction = input("Fraction: ").strip()
        convert_fraction = convert(fraction)

        if isinstance(convert_fraction, float):
            percentage = gauge(convert_fraction)
            return print(percentage)

        print(convert_fraction)


def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))

        if x > y or y == 0:
            pass

        resul = x / y
        return resul
    except ValueError:
        return f'ValueError'
    except ZeroDivisionError:
        return f'ZeroDivisionError'


def gauge(percentage):
    round_number = round(percentage * 100)

    match round_number:
        case 0 | 1:
            return 'E'
        case 99 | 100:
            return 'F'
        case _:
            return f'{round_number}%'


if __name__ == "__main__":
    main()
