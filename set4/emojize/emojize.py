import emoji

def get_emoji(msg):
    """
    This is an Fuction for print Emoji and do validation XD
    """
    try:
        print(emoji.emojize(msg, language='alias'))
    except:
        print(f"You have an Error \nVerified your Message")


def main():
    get_emoji(input("Input: "))


if __name__ == "__main__":
    main()
