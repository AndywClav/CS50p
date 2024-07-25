import inflect

names = []

while True:
    message = input("ok: ")
    if "" not in message:
        names.append(message)
    else:
        break

print(names)
