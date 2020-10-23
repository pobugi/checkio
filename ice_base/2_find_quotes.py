
# # """Your task at hand is to find all the quotes in a given text. And, as per usual, do everything as quickly as possible. 😉
# # You are given a string that consists of characters and a paired number of quotation marks. You need to return an Iterable 
# # consisting of the texts inside the quotation marks. But choose only quotes with double quotation marks ("). 
# # Single quotation marks (') aren’t appropriate.
# # """


# # s = 'good morning mister "superman" "pidor"'
# # # print(s)
# # # print(s.find('"'))

# # # i = 0
# # # while i <= len(s):
# # #     index = s.find('"')
# # #     s = s[index +1 :]
# # #     for  
# # #     # s = string
# # #     print(s)
# # #     i += 1

# # l = list(s)
# # print(l)
# # indices = []
# # for i in range(len(l)-2):
# #     if l[i] == '"':
# #         indices.append(i)
# #     l = l[i:]
# # print(indices)
# # res = []

# # for i in range(len(indices)):
# #     res.append(s[i:i+1])
    
# # print(res)


# import re
# def checkio(line: str) -> str:

#     words = re.split('[.,; ]', line)
#     count = 0
#     vowels = 'AEIOUY'.lower()
#     consonants = 'BCDFGHJKLMNPQRSTVWXZ'.lower()

#     def condition(s):
#         return len(s) > 1

#     def stripe(s):
#         s = s.lower()
#         for i in range(1, len(s)):
#             if (s[i] in consonants and s[i - 1] in vowels) or \
#                     (s[i] in vowels and s[i - 1] in consonants):
#                 continue
#             else:
#                 return False
#         return True

#     for word in words:
#         if condition(word) and stripe(word):
#             count += 1
#         return count



# if __name__ == '__main__':
#     print("Example:")
#     print(checkio('My name is ...'))

#     print(checkio('My name is ...'))
#     # assert checkio('Hello world') == 0
#     # assert checkio('A quantity of striped words.') == 1
#     # assert checkio('Dog,cat,mouse,bird.Human.') == 3
#     # print("Coding complete? Click 'Check' to earn cool rewards!")


s = 'abcdefg'
print(s[-4:])