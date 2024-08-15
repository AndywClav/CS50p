
def main():
    ...


def convert(fraction):
    while True:
        try:
            fraction = input("Fraction: ").strip()
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y or y == 0:
                continue
            resul = x / y
            return resul
        except ValueError:
            print(f'ValueError')
        except ZeroDivisionError:
            print(f'ZeroDivisionError')


def gauge(percentage):
    fraction = validation()
    percentage = round(fraction * 100)
    match percentage:
        case 0:
            print('E')
        case 1:
            print('E')
        case 25:
            print('25%')
        case 33:
            print('33%')
        case 50:
            print('50%')
        case 67:
            print('67%')
        case 75:
            print('75%')
        case 99:
            print('F')
        case 100:
            print('F')


if __name__ == "__main__":
    main()

