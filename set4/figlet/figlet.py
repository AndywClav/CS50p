from pyfiglet import Figlet
import sys

def text():
    if len(sys.argv):
        for arg in sys.argv:
            if arg == "-f" or arg == "--font":
                f = Figlet(sys.argv[2])
            else:
                f = Figlet()

def main():

message = input("Input: ")


print(f.renderText(message))
