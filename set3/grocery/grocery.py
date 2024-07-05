
def items():
    items = {}
    try:
        while True:
            item = input("").strip().lower()
            items[item] = 0
            if item in items:
                items[item] += 1
                print(f"{items[item]} {items.keys()}")
    except:
        return print(items)

items()
