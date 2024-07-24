from pyfiglet import Figlet
import sys

def font_text():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if len(sys.argv) > 2:
                try:
                    return Figlet(font=sys.argv[2])
                except Exception as e:
                    print(f"Error: {e}")
                    sys.exit(1)
            else:
                print("Error: Font name not provided.")
                sys.exit(1)
        else:
            print("Error: Invalid argument.")
            sys.exit(1)
    return Figlet()


def main():
    try:
        f = font_text()
        message = input("Input: ")
        print(f.renderText(message))
    except Exception as e:
        print(f"Error: {e}")
        f = Figlet(font='pawp')
        print(f.renderText('ERROR'))


if __name__ == "__main__":
    main()
