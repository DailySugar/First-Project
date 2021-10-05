'''
Created on Oct 2, 2021

@author: alexs
'''
import timeit


start = timeit.default_timer()


def sum_nat_numbers(num, sum=0, ssum=0):
    if num <= 0:
        return sum**2 - ssum
    else:
        return sum_nat_numbers(num - 1, sum + num, ssum + num**2)


print(sum_nat_numbers(100))


stop = timeit.default_timer()
print(stop-start)