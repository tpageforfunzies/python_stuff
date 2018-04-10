import test
import pytest


def increment(x):
    return x + 1


def f():
    raise SystemExit(1)


# testing function in this file
def test_increment():
    assert increment(4) == 5


# testing function from other hallway
def test_palindrome():
    assert test.is_palindrome("racecar")


def test_reverse():
    assert test.reverse("abcd") == "dcba"


# testing exception raising using the pytest class
def test_f():
    with pytest.raises(SystemExit):
        f()

def test_github1():
    assert len(test.github1()) == 138
