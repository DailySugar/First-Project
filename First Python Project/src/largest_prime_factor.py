"""
Created on Oct 2, 2021

@author: alexs
"""
import math


# The prime #s database starts empty. When the starting number, 2,
# is tested, nothing in the database can divide 2, so 2 gets added
# to the prime numbers list. The main idea here is that all divisible
# numbers out there are ultimately divisible by prime numbers.
nums = [2]


def check(num, lis = nums) -> bool:
    # Check if the # can be divided by something from the prime numbers database
    for y in lis:
        if num % y == 0:
            return False
        if y > math.sqrt(num):
            return True
    return True


num = 600851475143
# Without num+1, it'll only go up to 999 instead of 1000
for x in range(3, round(math.sqrt(num)), 2):
    if check(x) == False:
        # Not prime, move onto next number
        continue
    # Add to the prime numbers database
    nums.append(x)

for x in range(1, num // 2, 2):
    if num % x == 0:
        print(num // x, check(num // x))
    if num % x == 0 and check(num // x):
        print(num // x)
        break