"""
Not finished yet!
"""

# checkio("((5+3)*2+1)") == True
# checkio("{[(3+1)+2]+}") == True
# checkio("(3+{1-1)}") == False

s = "(abc(d)efg())"

# for i in range(len(s)):
#     open_brackets = s.count('(')
#     close_brackets = s.count(')')
#     print(s[i], end=' ')
# print()
# print(open_brackets, close_brackets)

def func(s):
    for i in range(len(s)):
        if s[i] == ')':
            break
    segment = s[:i+1]
    print(segment)
    for i in range(len(segment)-1, -1, -1):
        if segment[i] == '(':
            break
    print(segment[i:])

print(func(s))