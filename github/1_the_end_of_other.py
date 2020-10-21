"""For language training our Robots want to learn about suffixes.
In this task, you are given a set of words in lower case. Check whether there is a pair of words,
such that one word is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the
end of "hello", so the result is True."""


def checkio(words_set):
    words_set = list(words_set)
    if len(words_set) < 2:
        return False
    words_sorted = sorted(words_set, key=lambda word: len(word))

    for word in words_sorted:
        l = len(word)
        for words in words_sorted:
            if not word is words and word == words[-l:]:
                return True
    return False




if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
