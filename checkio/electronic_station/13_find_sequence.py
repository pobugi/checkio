"""You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits.
The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals)."""


s = [
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]

# for i in range(len(s)):
#     for j in range(len(s[i])):
#         if i == j:
#             print(s[i][j], end='')
#     print()


for i in range(len(s)):
    for j in range(len(s[i])):
            print(s[i][j], end='')
    print()


# for i in range(len(s)):
#     for j in range(len(s)):
#         print(s[j][i], end='')
#     print()