items = {}
item = input("").strip().lower()
contador = 0
items[item] = contador
if item in items:
    contador += 1
print(f"{items[item]} {items.keys()}")
