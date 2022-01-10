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