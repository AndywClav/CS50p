import inflect

p = inflect.engine()
names = []

while True:
    message = input("Name: ")
    if "" in message:
         break
    names.append(message)


print(f"Adieu, adieu, to {p.join(names)}")
