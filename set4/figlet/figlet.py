from pyfiglet import Figlet
import sys

def font_text():
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if arg == "-f" or arg == "--font":
                if i + 1 < len(sys.argv):
                    return Figlet(font=sys.argv[i + 1])
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
