"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or
phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from
another by rearranging the letters. Anagrams are case-insensitive and don't take account whitespaces.
For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrase. Try to verify are they anagrams or not.
"""


def verify_anagrams(a, b):
    sa = sorted(list(a.replace(' ', '').lower()))
    sb = sorted(list(b.replace(' ', '').lower()))

    return sa == sb


if __name__ == '__main__':
    print("Example:")
    print(verify_anagrams('Programming', 'Gram Ring Mop'))

    assert verify_anagrams('Programming', 'Gram Ring Mop') is True
    assert verify_anagrams('Hello', 'Ole Oh') is False
    assert verify_anagrams('Kyoto', 'Tokyo') is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
