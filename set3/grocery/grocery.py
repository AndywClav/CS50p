while True:
    item = input().strip()
    items = {}
    contador = 0
    if item == True:
        items[item]  # insert
        if items.get(item) == item:
            contador += 1


print(items)
