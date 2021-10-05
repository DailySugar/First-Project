'''
Created on Oct 4, 2021

@author: alexs
'''

import timeit


def largest_value(list, n = 0):
    #print(type(list[0]))
    if len(list) == 0:
        return n
    elif list[0] > n:
        return largest_value(list[1:], list[0])
    return largest_value(list[1:], n)


def largest_loop(list):
    """Most efficient of the three functions."""
    y = list[0]
    for x in list[1:]:
        if x > y:
            y = x
    return y
            

def largest(list):
    if len(list) == 1:
        return list[0]
    else:
        temp1 = list[0]
        temp2 = largest(list[1:])
        if temp1 >= temp2:
            return temp1
        else:
            return temp2
  
  
start = timeit.default_timer()  

list = [1231,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,12,312,312,123,123,213,132,23,12,132,231,123,321,123,123,213,123,231,132,213,1,12,1,1]

#print(largest_value(list))
print(largest_loop(list))
#print(largest(list))

stop = timeit.default_timer()
print(stop - start)