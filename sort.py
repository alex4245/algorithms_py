from copy import copy
import random

def bubble(lst):
    sort_lst = copy(lst)
    while True:
        change = False
        for i in range(len(sort_lst) - 1):
            if sort_lst[i] > sort_lst[i+1]:
                sort_lst[i], sort_lst[i+1] = sort_lst[i+1], sort_lst[i]
                change = True
        if not change:
            break
    return sort_lst


def shaker(lst):
    sort_lst = copy(lst)
    begin = 0
    end = len(sort_lst)
    while begin < end:
        for i in range(begin, end - 1):
            if sort_lst[i] > sort_lst[i + 1]:
                sort_lst[i], sort_lst[i + 1] = sort_lst[i + 1], sort_lst[i]
        end -= 1

        for i in range(end, begin, -1):
            if sort_lst[i] < sort_lst[i - 1]:
                sort_lst[i], sort_lst[i - 1] = sort_lst[i - 1], sort_lst[i]
        begin += 1
    return sort_lst

def quick_sort(lst):
    lst_len = len(lst)
    if lst_len < 2:
        return lst

    sort_lst = copy(lst)
    pivot = sort_lst.pop()
    left_lst = []
    right_lst = []
    for e in sort_lst:
        if e <= pivot:
            left_lst.append(e)
        else:
            right_lst.append(e)

    return quick_sort(left_lst) + [pivot] + quick_sort(right_lst)

def selection_sort(lst):
    sort_lst = copy(lst)
    for i in range(len(sort_lst) - 1):
        min_value = sort_lst[i]
        for j in range(i, len(sort_lst)):
            if sort_lst[j] < min_value:
                min_value = sort_lst[j]
        if sort_lst[i] == min_value:
            continue
        sort_lst.remove(min_value)
        sort_lst.insert(i, min_value)

    return sort_lst


lst = random.sample(range(1, 1000), 100)
b = bubble(lst)
sh = shaker(lst)
qs = quick_sort(lst)
ss = selection_sort(lst)
gs = sorted(lst)

assert gs == b
assert gs == sh
assert gs == qs
assert gs == ss
