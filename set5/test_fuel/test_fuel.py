from fuel import gauge, convert
import pytest


def test_gauge():
    # Test edge cases for gauge function
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'


def test_convert():
    # Test valid fractions
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1

    # Test edge cases
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("a/b")  # Invalid format


if __name__ == "__main__":
    pytest.main()
