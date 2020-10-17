"""You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should
have more elements. If it has no elements, then two empty arrays should be returned."""


def split_list(items: list) -> list:
    res = []
    if len(items) == 0:
        res.append([])
        res.append([])
    else:
        if len(items) % 2 == 0:
            splitter = len(items) // 2
        else:
            splitter = 1 + len(items) // 2
        first = items[:splitter]
        second = items[splitter:]
        res.append(first)
        res.append(second)
    return res


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
