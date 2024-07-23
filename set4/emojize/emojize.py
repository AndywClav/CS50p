import emoji

def emoji(emj):
    emoji.emojize(emj)

def inp():
    message = input("Input: ")
    if ":" in message:
        emj = message.split(":")
        emoji(emj)




print(f"Output {message}")
