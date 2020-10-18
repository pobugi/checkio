"""We have a List of booleans. Let's check if the majority of elements are true.

Some cases worth mentioning:
1) an empty list should return false;
2) if trues and falses have an equal amount, function should return false."""


def is_majority(items: list) -> bool:
    if not items:
        return False
    if items.count(True) <= items.count(False):
        return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    assert is_majority([True, True, False, True, False]) is True
    assert is_majority([True, True, False]) is True
    assert is_majority([True, True, False, False]) is False
    assert is_majority([True, True, False, False, False]) is False
    assert is_majority([False]) is False
    assert is_majority([True]) is True
    assert is_majority([]) is False
    print("Coding complete? Click 'Check' to earn cool rewards!")
