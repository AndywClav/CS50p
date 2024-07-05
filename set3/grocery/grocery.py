
def items():
    items = {}
    try:
        while True:
            item = input("").strip().lower()
            contador = 0
            items[item] = contador
            if item in items:
                contador += 1
                items.update({ item: contador })
                print(f"{items[item]} {items.keys()}")
    except:
        return print(items)

items()
