
def nested_sum(t):
    res = 0
    for el in t:
        num = sum(el)
        res += num
    print(res)


nested_sum([[1, 2], [3], [4, 5, 6]])


def cum_sum(t):
    res = []
    for el in t:
        res.append(sum(el))
    print(res)


cum_sum([[1, 2], [3], [4, 5, 6]])


def middle(t):
    res = t[1:-1]
    print(res)


middle([1, 2, 3, 4])


def chop(t):
    t.pop(0)
    t.pop(-1)
    print(t)


chop([1, 2, 3, 4])


def is_sorted(t):
    list = t[:]
    list.sort()
    print(t == list)


is_sorted([1, 2, 3])


def is_anagram(str_1, str_2):
    print(sorted(str_1) == sorted(str_2))


is_anagram('абвг', 'гвба')


def has_duplicates(s):
    res = list(s)
    res.sort()
    for i in range(len(res)-1):
        if res[i] == res[i+1]:
            return True
        return False

print(has_duplicates([1, 2, 3, 4]))


print(int(2),str('times'))

def diff_keys(old, new):
    d = {}
    d['kept'] = set(old) & set(new)
    d['added'] = set(new) - set(old)
    d['removed'] = set(old) - set(new)
    return d

def has_upper_case(text):
    for el in text:
        if el == el.upper():
            return True
        else:
            return False
print(has_upper_case("Hexlet"))

