"""You are given a string and two markers (the initial and final). You have to find a substring enclosed between these
two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string."""


def between_markers(text: str, marker1: str, marker2: str) -> str:

    if not marker1 and marker2:
        marker1 = text[0]
    if not marker2 and marker1:
        marker2 = text[-1]
    if not marker1 and not marker2:
        return text
    if text.find(marker1) > text.find(marker2) and (text.find(marker1) != -1 and text.find(marker2) != -1):
        return ''
    else:
        res = text.rpartition(marker1)
        res2 = res[-1].split(marker2)[0]
        return res2


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
