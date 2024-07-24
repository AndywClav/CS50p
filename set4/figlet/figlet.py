from pyfiglet import Figlet
import sys

def font_text():
    try:
        if len(sys.argv):
            for arg in sys.argv:
                if arg == "-f" or arg == "--font":
                    return Figlet(sys.argv[2])
                else:
                    return holaFiglet()
    except:
        print(f = pyfiglet.figlet_format("ERROR", font="doh"))


def main():
    f = font_text()
    message = input("Input: ")
    print(f.renderText(message))


if __name__ == "__main__":
    main()
