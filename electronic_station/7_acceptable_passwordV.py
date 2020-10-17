"""
In this mission you need to create a password verification function.

Those are the verification conditions:

    - the length should be bigger than 6;
    - should contain at least one digit, but it cannot consist of just digits;
    - having numbers or containing just numbers does not apply to the password longer than 9.
    - a string should not contain the word "password" in any case.
"""


def is_acceptable_password(password):
    if 'password' in password.lower():
        return False
    else:
        if password.isalpha():
            return len(password) >= 9
        elif password.isdigit():
            return len(password) >= 9
        elif len(password) > 6:
            alpha = False
            digit = False
            for char in password:
                if char.isdigit():
                    digit = True
                if char.isalpha():
                    alpha = True
            return alpha or digit
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    assert is_acceptable_password('short') is False
    assert is_acceptable_password('short54') is True
    assert is_acceptable_password('muchlonger') is True
    assert is_acceptable_password('ashort') is False
    assert is_acceptable_password('muchlonger5') is True
    assert is_acceptable_password('sh5') is False
    assert is_acceptable_password('1234567') is False
    assert is_acceptable_password('12345678910') is True
    assert is_acceptable_password('password12345') is False
    assert is_acceptable_password('PASSWORD12345') is False
    assert is_acceptable_password('pass1234word') is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
