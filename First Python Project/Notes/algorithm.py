import random

# Beatrice Wursley
# First phd thesis on modern computers. Founded school of computing in Queens

# U.K.L. - "We read to find out who we are."
# Everleest Gelwath
# "I'm gonna die in a duel"
# Wrote great math letter before dying in duel
# The best science books are the ones which the authors make clear how much they don't know.

# H.C - Hillary Clinton
# "It's time for us to move on from good words to good works."

# D.C - Dale Carnigey
# "People rarely succeed unless they're having fun with what they're doing."
# Proto-humans scratched prime numbers into some old bone?

# G.B - George Boole
# "The course of the world is not abandoned to chance."

# M.C. -
# "Be less curious about people, and be more curious about ideas."

# S.D - Shakuntala Davie - indian mathematician
# "Everything around you is mathematics."

# November 1, 2021      November 2, 2021        November 4, 2021        Nov 8
# Time to compute - assume all basic operations take the same amount of time
# Focus on worst case time
# Big O - Let f(n) & g(n) be functions
# where f(n) is in Order(g(n))
# Computational Complexity

# October 26, 2021      October 28, 2021
# Anthony Hoare's quicksort
# "If you had to think of a way to write something in a paper,
#  or say something in a speech, how would you do it?"
# "I would think of the way that I would say it, and that would be the best way."
#
# Choose a value from the list, and call it the pivot.
# Start with first value in list as pivot.
# Move all values > pivot to right hand side, and all values < pivot to left hand side.
#


# October 25, 2021
# Sorting functions
# Merge Sort: split into two equal sides and sort both sides, then merge both sides
def m_s(list, start, end):
    if start > end:
        return []
    elif start == end:
        return [list[start]]
    elif end - start == 1:
        return [list[start], list[end]] if list[start] < list[end] else [list[end], list[start]]
    else:
        left = m_s(list, start, (start + end - 1) // 2)
        right = m_s(list, (start + end + 1) // 2, end)
        # print(left,right)
        new_list = []
        while True:
            try:
                if left[0] < right[0]:
                    new_list.append(left[0])
                    left.pop(0)
                else:
                    new_list.append(right[0])
                    right.pop(0)
            except:
                if len(left) == 0:
                    return new_list + right
                else:
                    return new_list + left


def merge_sort(list):
    return m_s(list, 0, len(list) - 1)


print(merge_sort([1,5,8,1,5,9,1,2,4,324,234,234,423,35,73,2,1,423,3,5,263,4,512,4,123,125,132,421,5,63,47,24,1,32,2,56]))

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



