from pyfiglet import Figlet
import sys

if len(sys.argv):
    for x in sys.argv:
        if x == "-f" or x == "--font":
            print("aca")
    message = input("Input: ")
    f = Figlet()


print(f.renderText(message))
