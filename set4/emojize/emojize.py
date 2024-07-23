import emoji

def get_emoji():
    """
    This is an Fuction for print Emoji
    """
    try:
        messages = input("Input: ")
        print(emoji.emojize(messages, language='alias'))
    except:
        print(f"You have an Error \nVerified your Message")


def main():
    get_emoji()


if __name__ == "__main__":
    main()
