"""
In this mission you need to create a password verification function.
Those are the verification conditions:

    - the length should be bigger than 6;
    - should contain at least one digit.
"""


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        has_letter = False
        has_number = False

        for char in password:
            if char.isdigit():
                has_number = True
            if char.isalpha():
                has_letter = True
        return has_letter and has_number
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('muchlonger') is False
    assert is_acceptable_password('ashort') is False
    assert is_acceptable_password('muchlonger5') is True
    assert is_acceptable_password('sh5') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")