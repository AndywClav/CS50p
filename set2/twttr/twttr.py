twttr = input("Input: ").lower().strip()
vowels = ['a', 'e', 'i', 'o', 'u']
out = ""

for char in twttr:
    if char in vowels:
        continue
    else:
        out += char


print(out)
