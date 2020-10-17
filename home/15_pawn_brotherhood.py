"""
You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
"""


def safe_pawns(pawns: set) -> int:
    count = 0
    for i in pawns:
        defender1 = chr(ord(i[0]) - 1) + str(int(i[1]) - 1)
        defender2 = chr(ord(i[0]) + 1) + str(int(i[1]) - 1)
        if defender1 in pawns or defender2 in pawns:
            count += 1

    return count


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
