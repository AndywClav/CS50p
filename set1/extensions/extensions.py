filleIn = input("Fila name: ").lower().strip()
filleOut = filleIn.replace(".", "/")
part = filleOut.split('/')
exten = part[1]

if len(part) >= 2:
    match exten:
        case 'gif' | 'jpeg' | 'png':
            print('image/' + exten)
        case 'jpg':
            print('image/jpeg')
        case 'pdf' | 'zip':
            print('application/' + exten)
        case 'txt':
            print('text/plain')
        case _:
            print('application/octet-stream')


# the name the fille need change for image depend the format
