from test import is_palindrome

def increment(x):
    return x + 1


def test_answer():
    assert increment(4) == 5


def test_palidrome():
    assert is_palindrome("racecar") == True
