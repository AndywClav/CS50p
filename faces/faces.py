
def convert ():
    happy = '\U0001F642'
    sad = '\U0001F641' # Buscar la forma de colocar caras sin condicionales
    str = input()
    if (str == ':)'):
        print(chr(ord(happy)))
    elif (str == ':('):
        print(chr(ord(sad)))


convert()
