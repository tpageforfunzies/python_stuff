from test import is_palindrome
import pytest


def increment(x):
    return x + 1


def f():
    raise SystemExit(1)


# testing function in this file
def test_answer():
    assert increment(4) == 5


# testing function from other hallway
def test_palindrome():
    assert is_palindrome("racecar")


# testing exception raising using the pytest class
def test_f():
    with pytest.raises(SystemExit):
        f()
