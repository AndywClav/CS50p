from pyfiglet import Figlet
import sys

if len(sys.argv):
    for argum in sys.argv:
        if argum == "-f" or argum == "--font":
            #f = Figlet(sys.argv[3])
            print(argum)
        else:
            f = Figlet()

    message = input("Input: ")


print(f.renderText(message))
