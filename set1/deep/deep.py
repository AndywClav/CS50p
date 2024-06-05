deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
deep42 = deep.replace(' ', '')
if deep42 == '42' or deep == 'forty-two' or deep == 'forty two':
    print('Yes')
else:
    print('No')
