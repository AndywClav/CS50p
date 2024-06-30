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
    print(fraction)
    match fraction:
        case 0 or :
            print('E')
        case .25:
            print('25%')
        case .50:
            print('50%')
        case .75:
            print('75%')
        case 1 or 1.0 or .99:
            print('F')


main()
