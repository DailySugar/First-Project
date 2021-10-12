# October 10

main_number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
adjacent_digits = 13
nums = []
ans = 0
place = 0

for x in main_number:
    #print(x)
    #Skip to next set of numbers (nums) if there's a 0
    if x == '0':
        nums = []
        #print("clear")
        continue
    #Fill up the set of numbers (Will be one less if popped below)
    elif len(nums) < adjacent_digits:
        nums.insert(len(nums), int(x))
        #print(x, nums)
    #Once the set of numbers is filled, find the product of all the numbers and compare
    #to the currently largest number
    if len(nums) == adjacent_digits:
        #print(nums)
        compare = 1
        for y in nums:
            compare *= y
        if compare > ans:
            #print(nums, compare)
            ans = compare
        #print("pop")
        nums.pop(0)

print(ans)

"""
Less optimized, but functional version

#Scroll through all the numbers in num
while place < len(main_number):
    #Generate new set of adjacent digits
    while len(nums) < adjacent_digits:
        if main_number[place] == '0':
            if place >= len(main_number) - adjacent_digits:
                nums = [0]
                place = len(main_number)
                break
            else:
                nums = []
                place += 1
                continue
        else:
            nums.insert(len(nums), int(main_number[place]))
            place += 1
    #print(nums)
    #Compare product of old set with new set
    compare = 1
    for x in nums:
        compare *= x
    if compare > ans:
        ans = compare
        #print(nums, ans)
    #print(nums, place)
    nums.pop(0)
    #place = 1000
print(ans)
"""


#Thrown away code
# adjacent_digits = 13
#
#
# # First set of adjacent numbers
# def starting(start = 0, nums = []):
#     for x in num[start:adjacent_digits]:
#         if x == 0:
#             return starting(start + adjacent_digits)
#         nums.insert(len(nums), int(x))
#     return nums
#
#
# # Get next set of adjacent numbers, skipping if there's a 0
# def next(place = 0):
#     nums = []
#     if num[place] == 0:
#         return next(place + adjacent_digits)
#     else:
#         for x in num[place - adjacent_digits, place]:
#             nums.
#
#
# #Main function
# def largest_product(nums = [], ans = 1, compare = 1, place = adjacent_digits):
#     for x in range(adjacent_digits):
#         ans *= nums[x]
#     nums = next(place)
#     return ans, nums
#
#
# print(largest_product(starting()))
#
# # Prepare answer
# # for x in range(adjacent_digits):
# #     ans *= nums[x]
# #
# # for x in range(adjacent_digits, len(num)):
# #     temp = temp // nums[0] * int(num[x])
# #     nums.pop(0)
# #     nums.insert(len(nums), int(num[x]))
# #     if temp > ans:
# #         ans = temp
# #         print(ans, nums)
#
