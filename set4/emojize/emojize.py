import emoji

def main():
    try:
        messages = input("Input: ")
        print(emoji.emojize(messages, language='alias'))
    except OSError as err:
        print(err)

if __name__ == "__main__":
    main()
