from pyfiglet import Figlet
import sys

message = input("Input: ")

f = Figlet(font='slant')
print(f.renderText(message))
