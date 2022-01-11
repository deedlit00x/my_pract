# def apply_diff(target, diff):
#     for key in diff.keys():
#         if key == 'remove':
#             print(diff['remove'])
#             target.pop()
#             print(target)
#         if key == 'add':
#             print(diff['add'])
#     # remove = ''
#     # add = ''

# def apply_diff(target, diff):
#     set_for_update.update(diff.get('add', {}))
#     set_for_update.difference_update(diff.get('remove', {}))

# def greet(name, *args):
#     return 'Hello, {}!'.format(' and '.join((name,) + args))

# def normalize_url(url):
#     if url[:7] == "https:/":
#         return 'https://' + url[8:]
#     elif url[:7] == "http://":
#         return 'https://' + url[7:]
#     else:
#         return 'https://' + url

# print(normalize_url('ya.ru'))

# def print_numbers(num):
#     i = 0
#     while i != num:
#         print(num)
#         num -= 1
#     print('finished!')
# print_numbers(4)

# def join_numbers_from_range(start, stop):
#     result = ''
#     for el in range(start, stop + 1):
#         result += str(el)
#     strin = ''.join(result)
#     return f'{result}'

# print(join_numbers_from_range(5, 10))

# def encrypt(text):
#     i = 0
#     result = ""
#     while i < len(text):
#         nextChar = "" if (i + 1 >= len(text)) else text[i + 1]
#         result = result + nextChar + text[i]
#         i += 2
#     return result

# print(encrypt('text'))

# def reverse(string):
#     result = ''
#     for char in string:
#         result = char + result
#     return result

# reverse('go!')  # '!og'

# def filter_string(text, char):
#     upper_char = text.replace(char.upper(), '')
#     lower_char = upper_char.replace(char.lower(), '')
#     result = " ".join(lower_char.split())
#     return result

# print(filter_string('I look back if I am lost', 'o'))

# my_list = [12, 3, 456, 78]
# result = ''
# for el in my_list:
#     result += ''.join(str(el))

# print(result)

# def list_compare(list_1, list_2):
#     if len(list_1) == len(list_2):
#         if list_1 == list_2:
#             print('yes')
#         else:
#             print('no')
#         # i = 0
#         # while i < len(list_1):
#         #     for el in list_1:
#         #         if el in list_2:
#         #             list_2.remove(el)
#         #             print('yes')
#         #         else:
#         #             break
#         #     i += 1


# list_compare([12, 3, 456, 78], [12, 3, 456, 78])
