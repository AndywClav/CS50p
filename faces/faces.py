
def convert ():
    happy = '\U0001F642'
    sad = '\U0001F641' # Buscar la forma de colocar caras sin condicionales
    emoji = emoji.replace(":)", happy)
    emoji = emoji.replace(":(", sad)
    return emoji

def main ():
    message = input( f'ingrese un mensaje {convert()}')
    print(message, code)

main()
