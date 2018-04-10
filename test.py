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
    return new_word


def github1():
    nums = []
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            nums.append(str(i))
    print ",".join(nums)
    return nums


# print(var1)
# reverse(var1)
# print(is_balanced(var1))
# print(is_palindrome(var1))
github1()
