import sys
import emoji

try:
    print("hello, my name is", emoji.emojize(sys.argv[1]))
except error as er:
    print(er)
