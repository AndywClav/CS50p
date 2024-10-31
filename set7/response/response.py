from validator_collection import validators

def main():
    print(validation(input("What's your email address? ")))


def validation(em):
    try:
        validators.email(em)
        return f"Valid"
    except ValueError:
        return f"Invalid"


if __name__ == "__main__":
    main()
