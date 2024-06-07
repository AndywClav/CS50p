filleIn = input("Fila name: ").lower().strip()
filleOut = filleIn.replace(".", "/")
part = filleOut.split('/')
exten = part[1]

if len(part) >= 2:
    if 'gif' in filleOut or 'jpeg' in filleOut or 'png' in filleOut:
        print('image/' + exten)
    else:
        print('application/octet-stream')


# the name the fille need change for image depend the format
