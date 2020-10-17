"""
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks,
and/or contains at least one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.
"""


def is_stressful(s):
    if s.isupper():
        return True
    ending = s[-3:]
    if ending == '!!!':
        return True

    red_words_lower = []
    red_words = ['Help', 'asap', 'urgent']
    for word in red_words:
        red_words_lower.append(word.lower())

    s = s.split()

    def shrt(a):
        res = a[0]
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                pass
            else:
                res += a[i]
        return res

    for word in s:
        word = word.replace('-', '')
        word = word.replace('!', '')
        word = word.replace('.', '')
        word = shrt(word)
        if word.lower() in red_words_lower:
            return True
    return False


if __name__ == '__main__':
    assert is_stressful("Hi") is False, "First"
    assert is_stressful("I neeed HELP") is True, "Second"
    print('Done! Go Check it!')








