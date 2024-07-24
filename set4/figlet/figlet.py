from pyfiglet import Figlet
import sys

def font_text():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if len(sys.argv) > 2:
                return Figlet(font=sys.argv[2])
            else:
                sys.exit(1)
        else:
            sys.exit(1)
    return Figlet()


def main():
    try:
        f = font_text()
        message = input("Input: ")
        print(f.renderText(message))
    except:
        f = Figlet(font='pawp')
        print(f.renderText('ERROR'))


if __name__ == "__main__":
    main()
