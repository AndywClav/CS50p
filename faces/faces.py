
def convert ():
    happy = '\U0001F642'
    sad = '\U0001F641' # Buscar la forma de colocar caras sin condicionales
    str = input()
    if (str == ':)'):
        code = print(chr(ord(happy)))
        return code
    elif (str == ':('):
        code = print(chr(ord(sad)))
        return code

def main ():
    message = input( f'ingrese un mensaje {convert()}')
    print(message)

main()
