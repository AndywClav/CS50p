from pyfiglet import Figlet
import sys

def font_text():
    try:
        if len(sys.argv) > 1:
            for i, arg in enumerate(sys.argv):
                if arg == "-f" or arg == "--font":
                    if i + 1 < len(sys.argv):
                        font_name = sys.argv[i + 1]
                        return Figlet(font=font_name)
        return Figlet()
    except Exception as e:
        print(f"ERROR: {e}")
        return Figlet(font="doh")


def main():
    f = font_text()
    message = input("Input: ")
    print(f.renderText(message))


if __name__ == "__main__":
    main()
