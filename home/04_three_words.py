"""Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end"
contains three words in succession."""


def checkio(words: str) -> bool:
    lst = words.split()
    counter = 0
    for i in range(len(lst)):
        if counter == 3:
            break
        else:
            if lst[i].isalpha():
                counter += 1
            else:
                counter = 0
    return counter == 3


if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
