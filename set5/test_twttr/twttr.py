def shorten(word):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    out = ""

    for char in word:
        if char not in vowels:
            out += char

    return out


def main():
    twttr = input("Input: ").strip()
    shorten(twttr)


if __name__ == "__main__":
    main()
