"""
You are given a list of files. You need to sort this list by the file extension.
The files with the same extension should be sorted by name.

Some possible cases:

    - Filename cannot be an empty string;
    - Files without the extension should go before the files with one;
    - Filename ".config" has an empty extension and a name ".config";
    - Filename "config." has an empty extension and a name "config.";
    - Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
    - Filename ".imp.xls" has an extension "xls" and a name ".imp".
"""

from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    def ext(file):
        ext = ''
        for i in range(len(file)-1, -1, -1):
            if file[i] != '.':
                ext += file[i]
            else:
                break
        return ext[::-1]

    def filename(file: str):
        return file.split('.' + ext(file))[0]

    res = sorted(files, key=lambda x: (ext(x), filename(x)))
    empty = []
    others = []
    result = []

    for item in res:
        if filename(item) == '':
            empty.append(item)
        else:
            others.append(item)
    for item in empty:
        result.append(item)
    for item in others:
        result.append(item)
    return result


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
