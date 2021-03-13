"""You are given a text, which contains different English letters and punctuation marks. You should find the most
frequent letter in the text. The letter returned must be in lowercase.
During the search for the most wanted letter, casing doesn’t matter, "A" == "a". Make sure you don’t count in the
punctuation marks, digits and whitespaces, just letters.

If you have two or more letters occurring the same number of times, then return all of them as a list. For example --
"Hello, Evan" should return ['e', 'l']."""

from collections import Counter


def most_wanted(text: str) -> list:
    c = Counter()
    for char in text.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz':
            c[char] += 1
    c = dict(c)
    t = c.items()
    values = []
    for pair in t:
        values.append(pair[1])
    mx = max(values)
    res = []
    for item in t:
        if item[1] == mx:
            res.append(item[0])
    return res


if __name__ == '__main__':
    assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
    assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
    assert sorted(most_wanted("One")) == ["e", "n", "o"], "All letter only once."
    assert sorted(most_wanted("Oops!")) == ["o"], "Don't forget about lower case."
    assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
    assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
    print("Start the long test")
    assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."
    print("The local tests are done.")
