import emoji

message = input("Input: ")
if ":" in message:
    messa, icon = message.split(" ")
    print(icon)
    print(emoji.emojize(icon))
else:
    print(message)
