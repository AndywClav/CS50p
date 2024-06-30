def validation():
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


def main():
    fraction = validation()
    percentage = round(fraction * 100)
    match percentage:
        case 0:
            print('E')
        case 1:
            print('E')
        case 25:
            print('25%')
        case 50:
            print('50%')
        case 75:
            print('75%')
        case 99:
            print('F')
        case 100:
            print('F')


main()
