
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

def filter_map(f, iter):
    