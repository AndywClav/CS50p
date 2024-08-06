def shorten():
    twttr = input("Input: ").strip()
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    out = ""

    for char in twttr:
        if char not in vowels:
            out += char

    return out


def main():
    shorten()


if __name__ == "__main__":
    main()
