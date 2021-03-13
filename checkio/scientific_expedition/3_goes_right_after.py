"""In a given word you need to check if one symbol goes right after another.

Cases you should expect while solving this challenge:

    - If more than one symbol is in the list you should always count the first one
    - one of the symbols are not in the given word - your function should return False;
    - any symbol appears in a word more than once - use only the first one;
    - two symbols are the same - your function should return False;
    - the condition is case sensitive, which means 'a' and 'A' are two different symbols."""


def goes_after(text: str, first: str, second: str) -> bool:
    ind1 = text.find(first)
    ind2 = text.find(second)

    if (ind1 != -1 and ind2 != -1) and ind2 - ind1 == 1:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    assert goes_after('world', 'w', 'o') is True
    assert goes_after('world', 'w', 'r') is False
    assert goes_after('world', 'l', 'o') is False
    assert goes_after('panorama', 'a', 'n') is True
    assert goes_after('list', 'l', 'o') is False
    assert goes_after('', 'l', 'o') is False
    assert goes_after('list', 'l', 'l') is False
    assert goes_after('world', 'd', 'w') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")