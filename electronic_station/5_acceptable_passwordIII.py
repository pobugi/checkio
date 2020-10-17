"""
In this mission you need to create a password verification function.

Those are the verification conditions:

    - the length should be bigger than 6;
    - should contain at least one digit, but cannot consist of just digits.
"""


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        alpha = False
        digit = False
        for char in password:
            if char.isdigit():
                digit = True
            if char.isalpha():
                alpha = True
        return alpha and digit
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    assert is_acceptable_password('short') is False
    assert is_acceptable_password('muchlonger') is False
    assert is_acceptable_password('ashort') is False
    assert is_acceptable_password('muchlonger5') is True
    assert is_acceptable_password('sh5') is False
    assert is_acceptable_password('1234567') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")
