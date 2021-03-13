"""In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need
to determine.
When solving this task pay attention to the following points:

The words should be sought in all registers. This means that if you need to find a word "one" then words like
"one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value."""


def popular_words(text: str, words: list) -> dict:
    words_list = text.split()
    words_list_lower = []
    for word in words_list:
        words_list_lower.append(word.lower())

    d = dict((word, words_list_lower.count(word)) for word in words)
    return d


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
                        When I was One
                        I had just begun
                        When I was Two
                        I was nearly new
                        ''', ['i', 'was', 'three', 'near']))

    assert popular_words('''
                        When I was One
                        I had just begun
                        When I was Two
                        I was nearly new
                        ''', ['i', 'was', 'three', 'near']) == {
                                'i': 4,
                                'was': 3,
                                'three': 0,
                                'near': 0
                            }
    print("Coding complete? Click 'Check' to earn cool rewards!")
