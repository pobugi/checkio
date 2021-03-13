"""
In a given list the last element should become the first one.
An empty list or list with only one element should stay the same
"""


from typing import Iterable


def replace_last(items: list) -> Iterable:
    if items:
        res = []
        res.append(items[-1])
        for item in items[:-1]:
            res.append(item)
        return res
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_last([2, 3, 4, 1])))

    assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
