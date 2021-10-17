def first():
    lim = ['o', 'n', ' ', 't', 'a', 'p']
    phrase = "Don't panic!"
    plist = list(phrase)
    for i in range(4):
        plist.pop()

    plist.pop(0)
    plist.remove("'")
    plist.insert(2, plist.pop(3))
    plist.extend([plist.pop(), plist.pop()])
    new_phrase = ''.join(plist)
    print(new_phrase)


first()


def second():
    lim = ['o', 'n', ' ', 't', 'a', 'p']
    phrase = "Don't panic!"
    plist = list(phrase)
    new_phrase = ''.join(plist[1:3])
    new_phrase += ''.join([plist[5], plist[4], plist[7], plist[6]])
    print(new_phrase)


second()
