twttr = input("Input: ").lower().strip()
vowels = ['a', 'e', 'i', 'o', 'u',]
out = ""

for char in twttr:
    if char in vowels:
        out += char.remove(vowels, "")
        print(out)
    else:
        out += char



print(out)
