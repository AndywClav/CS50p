from plates import is_valid

def main():
    test_is_valid()


def test_is_valid():
    assert is_valid("CS50") == True


if __name == "__main__":
    main()
