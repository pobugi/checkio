"""Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python
format ("my_function_name") where all chars are in lowercase and all words are concatenated with an
intervening underscore symbol "_".
"""


def from_camel_case(text):
    res = text[0].lower()

    for i in range(1, len(text)):
        if text[i].isupper():
            res += '_' + text[i].lower()
        else:
            res += text[i]
    return res


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
