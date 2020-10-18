"""
In computer science and discrete mathematics, an inversion is a pair of places in a sequence where the elements in
these places are out of their natural order. So, if we use ascending order for a group of numbers, then an inversion
is when larger numbers appear before lower number in a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions
- 5 and 3;
- 5 and 4;
- 7 and 6.
You are given a sequence of unique numbers and you should count the number of inversions in this sequence.
"""


def count_inversion(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            if sequence[j] < sequence[i]:
                count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(count_inversion([1, 2, 5, 3, 4, 7, 6]))

    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
