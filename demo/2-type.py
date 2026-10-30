# import math
#
# r = float(input('place input the circle r:'))
#
# print(math.ceil(math.pi * r * r))
# print(math.ceil(math.pi * 2 * r))
#


# str1 = """hello world
#
# 666
# """
#
# # print(str1)
# #
# # print(str1.upper())
# # print(str1.islower())
# # print(str1.endswith('666\n'))
# #
# # str2 = str1.replace('666', 'python')
# # print(str2)
# # print(str1.split('\n'))
# #
# # print(len("Hello\nWorld!"))
#
# temp_str = ''
# str_len = len(temp_str)
# for i, s in enumerate(str1):
#     # print(str1[ str_len- i])
#     temp_str += str1[ str_len- i - 1]
#
# print(temp_str)


# 判断是否是回文
# def is_rev(s: str) -> bool:
#     temp_str = ''
#     s_len = len(s)
#     for (index, char) in enumerate(s):
#         temp_str += s[s_len - index - 1]
#     if (s == temp_str):
#         return True
#     return False
#
# str = input('please input your str: ')
#
# print(is_rev(str))


# 单词首字母大写
# def f(s: str):
#     str_list = s.split(' ')
#     for index, word in enumerate(str_list):
#         s0 = word[0].upper()
#         s1 = word[1:]
#         str_list[index] = s0 + s1
#     return ' '.join(str_list)
#
# print(f('hello world'))

# 是否是变位词
# def sort_str(s: str) -> str:
#     low_str = s.lower()
#     s_list = list(low_str)
#     s_list.sort()
#     return ''.join(s_list)
#
# def f(str1: str, str2:str) -> bool:
#     return sort_str(str1) == sort_str(str2)
#
# print(f('hello world', 'worldhello '))
#
# def f2(s: str) -> str:
#     new_str = sort_str(s)
#     c_map = {}
#     for c in new_str:
#         if c not in c_map:
#             c_map[c] = 1
#         else :
#             c_map[c] += 1
#
#     max = 0
#     for k, v in c_map.items():
#         if v > max:
#             max = v
#     return max
#
# print(f2('adfsafdaafdsafaaaaa'))


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-2:2:-3])  # 输出： ？？