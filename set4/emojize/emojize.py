import emoji

def main():
    try:
        messages = input("Input: ")
        print(emoji.emojize(messages, language='alias'))
    except Exception as e:
        print(f"Your error is {e}")

if __name__ == "__main__":
    main()
