"""YAML is a text, and you need to convert it into an object. But I’m not asking you to implement the entire YAML
standard, we’ll implement it step by step.
The first step is the key-value conversion. The key can be any string consisting of Latin letters and numbers.
The value can be a single-line string (which consists of spaces, Latin letters and numbers) or a number (int)."""


def yaml(a):
    lst = a.split('\n')
    d = {}
    for item in lst:
        if item:
            item = item.split(':')
            key = item[0].strip().rstrip()
            value = item[1].strip().rstrip()
            if value.isdigit():
                value = int(value)
            d.update({key: value})
    return d


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {
                    'age': 12,
                    'class': '12b',
                    'name': 'Alex Fox'
                   }
    print("Coding complete? Click 'Check' to earn cool rewards!")
