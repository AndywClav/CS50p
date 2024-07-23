import emoji

message = input("Input: ")
if ":" in message:
    messa, icon = message.split(":")
    print(emoji.emojize(messa, icon))
else:
    print(message)
