from validator_collection import validators

def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(email):
    """
    This function validates an email address. It prints "valid"
    if the email format is correct, otherwise it prints "invalid".
    """
    try:
        validators.email(email)
        return f"Valid"
    except ValueError:
        return f"Invalid"


if __name__ == "__main__":
    main()
