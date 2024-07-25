import inflect

p = inflect.engine()
names = []

while True:
    try:
        message = input("Name: ")
        if message == "":
            break
        names.append(message)
    except EOFError:
        break

if names:
    print(f"Adieu, adieu, to {p.join(names)}")
