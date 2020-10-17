"""You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it."""


def first_word(s: str) -> str:
    for char in [",", '.']:
        if char in s:
            s = s.replace(char, ' ')
    while s[0] == ' ':
        s = s[1:]
    first_space = s.find(' ')
    if first_space < 0:
        res = s
    else:
        res = s[:first_space]
    return res


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
