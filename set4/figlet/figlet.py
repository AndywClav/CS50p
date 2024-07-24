from pyfiglet import Figlet
import sys

if len(sys.argv):
    for arg in sys.argv:
        if arg == "-f" or arg == "--font":
            f = Figlet(sys.argv[2])
        else:
            f = Figlet()

    message = input("Input: ")


print(f.renderText(message))
