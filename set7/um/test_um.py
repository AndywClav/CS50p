from um import count

def main():
    test_count()
    test_error_count()


def test_count():
    assert count("Hello, um, world") == 1
    assert count("This is, um... CS50.") == 1
    assert count("Um... what are regular expressions? Um! XD") == 2


def test_error_count():
    assert count("are regular") == 0
    assert count(", u") == 0
    assert count("ello, yum, w") == 0


if __name__ == "__main__":
    main()
