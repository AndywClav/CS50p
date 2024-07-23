import emoji

def emoji(emj):
    return emoji.emojize(emj)

def inp():
    message = input("Input: ")
    if ":" in message:
        emj = message.split(":")
        emoj = emoji(emj)
        print(f"Output {emoj:thumbsup:}")
    else:
        print(message)

inp()
