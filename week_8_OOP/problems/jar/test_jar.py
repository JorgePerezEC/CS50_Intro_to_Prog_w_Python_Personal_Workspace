from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar("Hello")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(20)
    with pytest.raises(ValueError):
        jar.deposit(21)


def test_withdraw():
    jar = Jar(20)
    with pytest.raises(ValueError):
        jar.withdraw(21)
