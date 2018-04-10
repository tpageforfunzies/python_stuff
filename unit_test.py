import test, flip
import pytest
#paramterize to run multiple times for multiple inputs
#mark only works in > python3
# @pytest.mark.parametrize("test_input,expected", [
#     ("3+5", 8),
#     ("2+4", 6),
#     ("6*9", 42),
# ])


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

def test_flip():
    assert flip.printAllScreen() == 6

#only works in > python3
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
