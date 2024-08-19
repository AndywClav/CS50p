from fue import gauge


def main():
    test_fuel()


def test_fuel():
    assert gauge(1) == 'F'


if __name__ == "__main__":
    main()
