# Beatrice Wursley
# First phd thesis on modern computers. Founded school of computing in Queens

# U.K.L. - "We read to find out who we are."
# Everleest Gelwath
# "I'm gonna die in a duel"
# Wrote great math letter before dying in duel
# The best science books are the ones which the authors make clear how much they don't know.

import random

# October 25, 2021
# Sorting functions
# Merge Sort: split into two equal sides and sort both sides, then merge both sides
def m_s(list, start, end):
    if start > end:
        return []
    if start == end:
        return [list(start)]
    elif start - end == 1:
        return [list(start), list(end)] if list(start) < list(end) else [list(end), list(start)]
    else:
        left = m_s(list, start, (start + end) // 2)
        right = m_s(list, (start, end) // 2, end)
        new_list = []
        for x in range(len(left)):
            for y in right[x:]:
                if y <


def merge_sort(list):
    return m_s(list, 0, len(list))


# October 21, 2021
# Binary search
# def b_s_r(list, target, first, last):
#     if first <= last:
#         mid = (first + last) // 2
#         if list[mid] == target:
#             return mid
#         elif list[mid] > target:
#             return b_s_r(list, target, first, mid - 1)
#         else:
#             return b_s_r(list, target, mid + 1, last)
#     return - 1
#
#
# def binary_search(list, target):
#     return b_s_r(list, target, 0, len(list) - 1)
#
#
# print(binary_search([1,2,3,4,5,6,7,8,9,10], 9))

#October 18, 2021

# list_1 = [1]
# list_2 = ['a']
# list_3 = [True]
# list_4 = ["llama"]
# list_5 = ["lovelace"]
#
# lists = [list_1, list_2, list_3, list_4, list_5]
#
# for i in range(20):
#     x, y = random.sample(range(5), 2)
#     lists[x].append(lists[y][:])
#
# for i in lists:
#     print(i)



