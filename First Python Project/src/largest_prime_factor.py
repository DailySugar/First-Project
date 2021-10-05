'''
Created on Oct 2, 2021

@author: alexs
'''

def check(num,lis):
    # Check if the # can be divided by something from the prime numbers database
    for y in lis:
        if num%y==0:
            return True

def largest_prime_factor(num,test):
    nums=[]
    for x in range(2,num+1):
        if check(x,nums):
            # Not prime, move onto next number
            continue
        # Add to the prime numbers database
        nums.append(x)