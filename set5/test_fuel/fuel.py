def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)


def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))

        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")

        result = round((x / y) * 100)
        return result

    except ValueError:
        raise ValueError("Invalid input. Both numerator and denominator must be integers.")


def gauge(percentage):
    match percentage:
        case 0 | 1:
            return 'E'
        case 99 | 100:
            return 'F'
        case _:
            return f'{percentage}%'


if __name__ == "__main__":
    main()
