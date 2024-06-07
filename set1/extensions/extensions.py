filleIn = input("Fila ame: ").lower()
FilleOut = filleIn.replace(".", "/").strip()
FilleOut.split('/')

# Verificar que se hayan ingresado exactamente dos partes
if len(FilleOut) == 2:
    subtipo = FilleOut[1]
    print("El subtipo ingresado es:", subtipo)
else:
    print("El formato ingresado no es válido.", FilleOut[0])

# if 'gif' in FilleOut or 'jpg' in FilleOut or 'jpeg' in FilleOut or 'png' in FilleOut:
#     print('image/')
# else:
#     print('')


# the name the fille need change for image depend the format
