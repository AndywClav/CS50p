import emoji

def main():
    try:
        messages = input("Input: ")
        print(emoji.emojize(messages, language='alias'))
    except:
        print("Your error is")

if __name__ == "__main__":
    main()
