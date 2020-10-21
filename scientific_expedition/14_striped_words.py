"""Our robots are always working to improve their linguistic skills. For this mission,
they research the Latin alphabet and its applications.

The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by whitespaces and punctuation marks.
Numbers are not considered as words in this mission (a mix of letters and digits is not a word either).
You should count the number of words (striped words) where the vowels with consonants are alternating;
words that you count cannot have two consecutive vowels or consonants.
The words consisting of a single letter are not striped -- don't count those.
Casing is not significant for this mission."""

import re


def checkio(line: str) -> int:
    vowels = 'AEIOUY'.lower()
    consonants = 'BCDFGHJKLMNPQRSTVWXZ'.lower()

    def condition(s):
        return len(s) > 1

    def stripe(s):
        s = s.lower()
        for i in range(1, len(s)):
            if (s[i] in consonants and s[i - 1] in vowels) or \
                    (s[i] in vowels and s[i - 1] in consonants):
                continue
            else:
                return False
        return True

    words = re.split('[.,;? ]', line)
    count = 0
    for word in words:
        if condition(word) and stripe(word):
            count += 1
            print(word)
    return count


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")


