twttr = input("Input: ").lower().strip()
vowels = ['a', 'e', 'i', 'o', 'u']
out = ""

for char in twttr:
    if char not in vowels:
        out += char


print(out)
