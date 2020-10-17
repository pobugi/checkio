"""Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the
key “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure
the accents, he is more careful in the presence of such raffinated characters ([Shift] + [Char])
and will press the keys correctly.) Compute and return the result of having Joe type in the given text.
The “Caps Lock” key affects only the letter keys from “a” to “z” , and has no effect on the other keys or characters.
“Caps Lock” key is assumed to be initially off.
"""


def caps_lock(txt: str) -> str:
    vowels = 'a'
    res = ''
    i = 0
    switch = 0
    while i <= len(txt) - 1:
        if txt[i] in vowels:
            switch = abs(switch-1)

        if switch == 1:
            if not txt[i] in vowels:
                res += txt[i].upper()
        else:
            if not txt[i] in vowels:
                res += txt[i]
        i += 1
    return res


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
