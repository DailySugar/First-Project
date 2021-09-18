'''
Created on Sep 17, 2021

@author: alexs
'''

def check(num,lis):
    # Check if the # can be divided by something from the prime numbers database
    for y in lis:
        if num%y==0:
            return True
        
num=1000
# The prime #s database starts empty. When the starting number, 2,
# is tested, nothing in the database can divide 2, so 2 gets added
# to the prime numbers list. The main idea here is that all divisible
# numbers out there are ultimately divisible by prime numbers.
nums=[]
# Without num+1, it'll only go up to 999 instead of 1000
for x in range(2,num+1):
    if check(x,nums):
        # Not prime, move onto next number
        continue
    # Add to the prime numbers database
    nums.append(x)
    print(x)
print(nums)
