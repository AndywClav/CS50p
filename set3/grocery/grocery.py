
def items():
    items = {}
    try:
        while True:
            item = input("").strip().lower()
            contador = 0
            items[item] = contador
            if item in items:
                items.update({item: contador + 1})
                print(f"{items[item]} {items.keys()}")
    except KeyboardInterrupt:
        return 0

items()
