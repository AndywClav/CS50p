from plates import is_valid

def main():
    test_is_valid()


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("ECTO88") == True
    assert is_valid("50") == False
    assert is_valid("") == True
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()
