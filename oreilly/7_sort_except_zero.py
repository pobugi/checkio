"""
Sort the numbers in an array. But the position of zeros should not be changed.
"""


from typing import Iterable


def except_zero(items: list) -> Iterable:
    zero_indexes = []
    zero_qty = items.count(0)
    for i in range(len(items)):
        if not items[i]:
            zero_indexes.append(i)
    items.sort()
    items = items[zero_qty:]
    for index in zero_indexes:
        items.insert(index, 0)
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
