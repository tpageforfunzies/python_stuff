# import sys
# var1 = sys.argv[1]


def is_balanced(param):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    if not param:
        return False
    for char in param:
        if char == "{" or char == "(" or char == "[":
            stack.append(char)
        else:
            try:
                popped = stack.pop()
            except:
                return False
            if pairs[popped] != char:
                return False
            else:
                return True


def is_palindrome(param):
    if not param:
        return False
    for char in range(len(param)):
        if param[char] == param[(len(param) - 1) - char]:
            print(param[char])
        else:
            return False

    return True


def reverse(param):
    new_word = ""
    for char in range(len(param)):
        new_word += param[(len(param) - 1) - char]
        print(new_word)


# print(var1)
# reverse(var1)
# print(is_balanced(var1))
# print(is_palindrome(var1))

