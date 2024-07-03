items = {}
contador = 0

while True:
    try:
        item = input().strip()
        if item == True:
            items[item]  # insert
            if items.get(item) == item:
                contador += 1
    except KeyError:
        pass
    except KeyboardInterrupt:
        print(items)
        break



