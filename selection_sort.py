from copy import deepcopy

l = [
        {'Audi': 13},
        {'Mercedes': 5},
        {'Renault': 3},
        {'Toyota': 31},
        {'Honda': 18},
        {'Ford': 14},
]


def find_smallest(l):
    smallest = next(l[0].iteritems())
    s_p = 0
    for i, e in enumerate(l):
        s = next(e.iteritems())
        if s[1] < smallest[1]:
            smallest = s
            s_p = i
    return s_p, smallest

def ssort(l):
    l = deepcopy(l)
    new_l = []
    while l:
        pos, n = find_smallest(l)
        new_l.append(dict([n]))
        l.pop(pos)
    return new_l


print(ssort(l))
