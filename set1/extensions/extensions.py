filleIn = input("Fila name: ").lower().strip()
FilleOut = filleIn.replace(".", "/")
FilleOut.split('/')
subtipo = FilleOut[0]

print(subtipo)

filleIn = input("Fila name: ").lower().strip()
filleOut = filleIn.replace(".", "/")
partes = filleOut.split('/')

# Obtener la primera parte
subtipo = partes[0]

print("El tipo ingresado es:", subtipo)

# # Verificar que se hayan ingresado exactamente dos partes
# if len(FilleOut) > 2:
#     subtipo = FilleOut[1]
# else:
#     print("El formato ingresado no es válido.", FilleOut)

# if 'gif' in FilleOut or 'jpg' in FilleOut or 'jpeg' in FilleOut or 'png' in FilleOut:
#     print('image/')
# else:
#     print('')


# the name the fille need change for image depend the format
