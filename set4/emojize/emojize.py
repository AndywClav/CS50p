import emoji

def emoji(emj):
    return emoji.emojize(emj)

def inp():
    message = input("Input: ")
    if ":" in message:
        emj = message.split(":")
        emoji = emoji(emj)
        print(f"Output {message}{emoji}")

inp()
