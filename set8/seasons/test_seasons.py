from seasons import MinutesLived
import pytest

def main() -> None:
    test_MinutesLived()
    test_error_MinutesLived()


def test_minutes_lived() -> None:
    assert str(MinutesLived('1999-01-01')) == 'Thirteen million, seven hundred seven thousand, three hundred sixty minutes'


def test_error_minutes_lived() -> None:
    with pytest.raises(SystemExit):
        MinutesLived("January 1, 1999")
    with pytest.raises(SystemExit):
        MinutesLived("3000-01-01")


if __name__ == '__main__':
    main()
