
def convert (emoji):
    happy = '\U0001F642'
    sad = '\U0001F641' # Buscar la forma de colocar caras sin condicionales
    emoji = emoji.replace(":)", chr(ord(happy)))
    emoji = emoji.replace(":(", chr(ord(sad)))
    return emoji

def main ():
    message = input(': ')
    if (message)
    print(message,)

main()
