"""
You are given some text potentially including sensible words. You should count how many words are included in the
given text. A word should be whole and may be a part of other word. Text letter case does not matter.
Words are given in lowercase and don't repeat. If a word appears several times in the text,
it should be counted only once.

For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.
"""


def count_words(text: str, words: set) -> int:
    res = 0
    for word in words:
        if word.lower() in text.lower():
            res += 1
    return res


if __name__ == '__main__':
    print("Example:")
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))

    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
