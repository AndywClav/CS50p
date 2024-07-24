from pyfiglet import Figlet
import sys

if len(sys.argv):
    for x in sys.argv:
        if x == "-f" or x == "--font":
            f = Figlet()
        else:
        f = Figlet()

    message = input("Input: ")


print(f.renderText(message))
