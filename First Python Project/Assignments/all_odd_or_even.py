"""
Created on Oct 1, 2021
Author: Alex Sun
Student Number: 20289530
CISC-121

All this work is mine. No Ctrl+C Ctrl+V here.
"""


def all_odd_or_even(*args):
    """
        Accepts any # of arguments and returns true if there's
        at least 1 argument and they're either all even or
        all odd integers.
    """
    if len(args) < 1:
        return False
    for num in args:
        if type(num) is not int:
            return False
        elif num % 2 == 0:
            continue
        else:
            for num in args:
                if type(num) is not int:
                    return False
                elif num % 2 == 1:
                    continue
                else:
                    return False
            return True
    return True


#Enter your args here
print(all_odd_or_even(1,2,3,4))