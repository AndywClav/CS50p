twttr = input("Input: ").strip()
vowels = ['a', 'e', 'i', 'o', 'u',]

for char in twttr:
    if char == vowels:
        print("vowels")
    else:
        print("UnVowels")
