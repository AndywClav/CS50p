from pyfiglet import Figlet
import sys

def font_text():
    if len(sys.argv):
        for arg in sys.argv:
            if arg == "-f" or arg == "--font":
                return Figlet(sys.argv[2])
            else:
                sys.exit


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
