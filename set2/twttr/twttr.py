twttr = input("Input: ").strip()
vowels = ['a', 'e', 'i', 'o', 'u',]
out = ""

for char in twttr:
    if char in vowels:
        out += char
        print(out)
    else:
        out += char



print(out)
