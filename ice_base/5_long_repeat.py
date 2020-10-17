"""
There are four substring missions that were born all in one day and you shouldn’t need more than one day to solve them.
All of these missions can be simply solved by brute force, but is it always the best way to go?

This mission is the first one of the series.
Here you should find the length of the longest substring that consists of the same letter.
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
The last substring is the longest one, which makes it the answer.
"""


def long_repeat(s: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    if s:
        maxcount = 1
        count = 1
        i = 1
        while i < len(s):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            if count > maxcount:
                maxcount = count
            i += 1
        return maxcount
    return 0


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
