"""In a given string you should reverse every word, but the words should stay in their places."""


def backward_string_by_word(words: str) -> str:
    words_list = words.split(' ')
    for i in range(len(words_list)):
        words_list[i] = words_list[i][::-1]
    return ' '.join(words_list)


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
