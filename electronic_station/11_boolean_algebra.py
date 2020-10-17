"""
You are given two boolean values x and y as 1 or 0 and you are given an operation name as described earlier.
You should calculate the value and return it as 1 or 0.
"""


OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == 'conjunction':
        return x and y
    elif operation == 'disjunction':
        return x or y
    elif operation == 'implication':
        return y if x else 1
    elif operation == 'exclusive':
        return x != y
    elif operation == 'equivalence':
        return x is y


if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')
