"""Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name")
into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated
without any intervening characters."""


def to_camel_case(text):
    res = text[0].upper()
    i = 1
    while i <= len(text)-1:
        if text[i] == '_':
            res += text[i+1].upper()
            i += 1
        else:
            res += text[i]
        i += 1
    return res


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
