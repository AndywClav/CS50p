import inflect

p = inflect.engine()
names = []

while True:
    message = input("ok: ")
    if " " not in message:
        names.append(message)
    else:
        break

print(p.join(names))
print(names)
