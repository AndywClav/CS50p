filleIn = input("Fila name: ").lower().strip()
filleOut = filleIn.replace(".", "/")
part = filleOut.split('/')
subtipo = part[0]
exten = part[1]

if len(part) > 2:
    if 'gif' in filleOut or 'jpg' in filleOut or 'jpeg' in filleOut or 'png' in filleOut:
        print('image/', exten)
    else:
        print('')


# the name the fille need change for image depend the format
