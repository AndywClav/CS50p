from pyfiglet import Figlet
import sys

if len(sys.argv):
    for arg in sys.argv:
        if arg == "-f" or arg == "--font":
            for i in sys.argv:
            #f = Figlet(sys.argv[3])
            print(i)
        else:
            f = Figlet()

    message = input("Input: ")


print(f.renderText(message))
