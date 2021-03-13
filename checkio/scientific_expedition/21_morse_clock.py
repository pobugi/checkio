"""
Help Stephen to create a module for converting a normal time string to a morse time string. As you can see in the
illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a
different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a
length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes
and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every
on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".")."""


import requests

morse_url = "https://gist.githubusercontent.com/mohayonao/094c71af14fe4791c5dd/raw/8399262545d0d88507ce42069b0b50043f0eddbc/morse-code.json"

res = requests.get(morse_url).json()
print(type(res))

s = "10:37:49"
c = []
for char in s:
    if char == ':':
        c.append(':')
    else:
        c.append(res[char])
print('c = ', c)