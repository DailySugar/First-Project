# Beatrice Wursley
# First phd thesis on modern computers. Founded school of computing in Queens

# U.K.L. - "We read to find out who we are."

import random

# October 21, 2021
# Binary search
def b_s_r(list, target, first, last):
    if first <= last:
        mid = (first + last) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            return b_s_r(list, target, first, mid - 1)
        else:
            return b_s_r(list, target, mid + 1, last)
    return - 1


def binary_search(list, target):
    return b_s_r(list, target, 0, len(list) - 1)


print(binary_search([1,2,3,4,5,6,7,8,9,10], 9))

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



