"""Your task at hand is to find all the quotes in a given text. And, as per usual, do everything as quickly as possible. 😉
You are given a string that consists of characters and a paired number of quotation marks. You need to return an
Iterable consisting of the texts inside the quotation marks. But choose only quotes with double quotation marks (").
Single quotation marks (') aren’t appropriate.
"""


def find_quotes(s):
    indices = []
    for i in range(len(s)):
        if s[i] == '"':
            indices.append(i)
    res = []
    i = 0
    while i < len(indices):
        start = indices[i] + 1
        end = indices[i + 1]
        res.append(s[start:end])
        i += 2
    return res


if __name__ == '__main__':
    print("Example:")
    print(find_quotes('"Greetings"'))

    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
                         'of the printing and typesetting '
                         'industry. Lorem Ipsum has been the '
                         '"industry\'s standard dummy text '
                         'ever since the 1500s", when an '
                         'unknown printer took a galley of '
                         'type and scrambled it to make a type '
                         'specimen book. It has survived not '
                         'only five centuries, but also the '
                         'leap into electronic typesetting, '
                         'remaining essentially unchanged. "It '
                         'was popularised in the 1960s" with '
                         'the release of Letraset sheets '
                         'containing Lorem Ipsum passages, and '
                         'more recently with desktop '
                         'publishing software like Aldus '
                         'PageMaker including versions of '
                         'Lorem Ipsum.') == ['Lorem Ipsum',
                         "industry's standard dummy text ever "
                         'since the 1500s',
                         'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']
    print("Coding complete? Click 'Check' to earn cool rewards!")