import emoji

message = input("Input: ")
if ":" in message:
    #messa, icon = message.split(" ")
    #print(icon)
    icon = emoji.emojize(message)
    print(f"Hola {icon}")
else:
    print(message)
