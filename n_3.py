
# def get_colors():
#     def rgb(red=0, green=0, blue=0):
#         return 'rgb({}, {}, {})'.format(red, green, blue)
#     return {
#         'red': rgb(red=255),
#         'green': rgb(green=255),
#         'blue': rgb(blue=255),
#     }

# d = {'a': 1, 'b': None, 2: 4}

# def updated(dict, **kwargs):
#     tmp_dict = kwargs
#     tmp = dict.copy()
#     tmp.update(tmp_dict)
#     return tmp

# print(updated(d, a=2, b=True, c=None))

# def call_twice(func, *args, **kwargs):
#     first_f = func(*args, **kwargs)
#     second_f = func(*args, **kwargs)
#     return first_f, second_f


# user_input = int(input('number pls: '))

# tmp = []
# for el in range(user_input):
#     tmp.append(el + 1)
# result = tuple(tmp)
# print(result)


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# print(change([1, 2, 3, 4, 5]))


# def list_sort(lst):
#     lst.sort(reverse = False)
#     return lst

# print(list_sort([1, 5, 77]))


# phrase = "Don't panic!"
# plist = list(phrase)
# new_phrase = ''.join(plist[1:3])
# new_phrase += ''.join([plist[5],plist[4],plist[7],plist[6]])
# print(new_phrase)


# vowels = ['a','o','i','u','e']
# word = input('provide a word: ')
# found =  {
#     'a': 0,
#     'o': 0,
#     'i': 0,
#     'e': 0,
#     'u': 0,
# }

# for letter in word:
#     if letter in vowels:
#         found[letter] += 1

# print(found)

# fruits = {'apples' : 1}

# fruits.update({'bananas' : 1})


# print(fruits.items())


# def filter_map(function, items):
#     result = []
#     for item in items:
#         keep, value = function(item)
#         if keep:
#             result.append(value)
#     return result

# print(list(filter(None, ['', 1, 2, 'foo', None, False])))


# def keep_truthful(iter):
#     tmp = list(map(bool, iter))
#     res = list(filter(lambda x: x == True, tmp))
#     return res


# print(keep_truthful([True, False, 1, "", "foo"]))

# def abs_sum(iter):
#     tmp = list(map(abs, iter))
#     return sum(tmp)

# print(abs_sum([-3, 7]))

# from functools import reduce
# from operator import getitem, truth


# def keep_truthful(items):
#     return filter(truth, items)


# def abs_sum(numbers):
#     return sum(map(abs, numbers))


# def walk(dictionary, path):
#     return reduce(getitem, path, dictionary)



