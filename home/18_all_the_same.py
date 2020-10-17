"""
In this mission you should check if all elements in the given list are equal.
"""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if not elements:
        return True
    else:
        if len(set(elements)) == 1:
            return True
        return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    assert all_the_same([1, 1, 1]) is True
    assert all_the_same([1, 2, 1]) is False
    assert all_the_same(['a', 'a', 'a']) is True
    assert all_the_same([]) is True
    assert all_the_same([1]) is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
