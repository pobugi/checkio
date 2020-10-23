"""Create and return a new iterable that contains the same elements as the argument iterable items, but with the
reversed order of the elements inside every maximal strictly ascending sublist. This function should not modify
the contents of the original iterable."""


def reverse_ascending(items):
    if items == sorted(items, reverse=True):
        return items
    if items == sorted(items):
        return items[::-1]
    else:
        i = 0
        list = []
        res = []
        while i < len(items) - 1:
            if items[i + 1] > items[i]:
                list.append(items[i])
            else:
                list.append(items[i])
                list = list[::-1]
                res += list
                list = []

            i += 1
        print(res)
        if len(res) < len(items):
            if list[0] < items[-1]:
                res += [items[-1], list[0]]
            else:
                res += [list[0], items[-1]]
    return res

print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])

# if __name__ == '__main__':
#     print("Example:")
#     print(reverse_ascending([1, 2, 3, 4, 5]))
#
#     assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
#     assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
#     assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
#     assert list(reverse_ascending([])) == []
#     assert list(reverse_ascending([1])) == [1]
#     assert list(reverse_ascending([1, 1])) == [1, 1]
#     assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
