twttr = input("Input: ").strip()
vowels = ['a', 'e', 'i', 'o', 'u',]
out = ""

for char in twttr:
    if char in vowels:
        print(out)
        out = twttr.replace(char, "") + char
        print(out)


