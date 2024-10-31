from validator_collection import validators

def main():
    print(validation_email(input("What's your email address? ")))


def validation_email(s):
    """
    This function do a valid to email if the email is
    correct print valid else print invalid
    """
    try:
        validators.email(s)
        return f"Valid"
    except ValueError:
        return f"Invalid"


if __name__ == "__main__":
    main()
