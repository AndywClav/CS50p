from plates import is_valid

def main():
    test_is_valid_true()
    test_is_valid_false()


def test_is_valid_true():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True


def test_is_valid_false():
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()
