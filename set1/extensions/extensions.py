filleIn = input("Fila ame: ").lower()
FilleOut = filleIn.replace(".", "/").strip()
if 'gif' in FilleOut or 'jpg' in FilleOut or 'jpeg' in FilleOut or 'png' in FilleOut:
    print('image/')
else:
    print('')


# the name the fille need change for image depend the format
