items = {}
while True:
    try:
        item = input().strip()
        contador = 0
        if item == True:
            items[item]  # insert
            if items.get(item) == item:
                contador += 1
    except KeyError:
        continue
    except KeyboardInterrupt:
        continue


print(items)
