from pyfiglet import Figlet
import sys

def font_text():
    try:
        if len(sys.argv):
            for arg in sys.argv:
                if arg == "-f" or arg == "--font":
                    return f = Figlet(sys.argv[2])
                else:
                    return f = Figlet()
    except:
        print(f = pyfiglet.figlet_format("ERROR", font="doh"))

def main():
    font_text()
    message = input("Input: ")
    print(f.renderText(message))
