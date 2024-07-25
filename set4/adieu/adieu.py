import inflect

names = []

while True:
    message = input("ok: ")
    if "-1" not in message:
        names = message
    else:
        break

print(names)
