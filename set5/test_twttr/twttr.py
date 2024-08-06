def shorten(word):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    out = ""

    for char in word:
        if char not in vowels:
            out += char

    return out


def main():
    word = input("Input: ").strip()
    twttr = shorten(word)
    print(twttr)


if __name__ == "__main__":
    main()
