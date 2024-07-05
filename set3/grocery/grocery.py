items = {}
while True:
    item = input("").strip().lower()
    contador = 0
    items[item] = contador
    if item in items:
        items[item] = contador + 1


print(f"{items[item]} {items.keys()}")
