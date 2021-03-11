"""
You need to check that the 2 given strings are isometric. 
This means that a character from one string can become a match
for characters from another string.

One character from one string can correspond only to one character from another string. 
Two or more characters of one
string can correspond to one character of another string, but not vice versa.
"""


def isometric_strings(str1: str, str2: str) -> bool:
    if not str1 and not str2:
        return True
    if len(set(str1)) == len(set(str2)):
        if str2[0] + str2[1:] == str2 and str1[0] + str1[1:]:
            return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    assert isometric_strings('add', 'egg') is True
    assert isometric_strings('foo', 'bar') is False
    assert isometric_strings('', '') is True
    assert isometric_strings('all', 'all') is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
