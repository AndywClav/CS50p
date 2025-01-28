from jar import Jar
import pytest

jar = Jar()

def test_init():
    with pytest.raises(ValueError):
        jar.__init__("It should be a number")


def test_str():
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    jar.deposit(3)
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"
