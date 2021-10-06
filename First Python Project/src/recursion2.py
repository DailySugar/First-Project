'''
Created on Oct 5, 2021

@author: alexs
'''

import timeit


def exponent_recursive(x, y):
    if y == 0:
        return 1
    else: return x * exponent_recursive(x, y - 1)
 
 
def exponent_special(x, y):
    if y == 0:
        return 1
    if y == 2:
        return x * x
    return exponent_special(exponent_special(x, y // 2), 2)
    
    
def exponent_iterative(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result


start = timeit.default_timer()

print(exponent_special(2, 11))

stop = timeit.default_timer()
print(stop - start)