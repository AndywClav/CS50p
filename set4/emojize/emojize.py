import emoji

def main():
    """
    This is an exemple 
    """
    try:
        messages = input("Input: ")
        print(emoji.emojize(messages, language='alias'))
    except:
        print(f"You have an Error \nVerified your Message")

if __name__ == "__main__":
    main()
