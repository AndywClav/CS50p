import inflect

p = inflect.engine()
names = []

while True:
    message = input("ok: ")
    if "-1" not in message:
        names.append(message)
    else:
        break

# print(p.join(names))
print(names)
