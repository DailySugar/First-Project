"""
Created October 26, 2021
Alex Sun
20289530
CISC-121

Converting between recursive and non-recursive functions, and
optimizing recursive functions.
"""


# Part 1

# For each of the non-recursive functions given here, create
# a recursive function that produces the same result

# Problem 1:

def exponent(x, y):  # y is a positive integer
    ''' compute x^y, where y is a positive integer '''
    result = x
    while y > 1:
        result = result * result
        if (y % 2 == 1):
            result *= x
        y = y // 2
    return result


def exponent_rec(x, y):
    return


# Problem 2:

def sublist_sum(a_list, target):
    ''' determine if list a_list has a consecutive sub-list that sums to target '''
    for start in range(len(a_list)):
        sum = 0
        for finish in range(start, len(a_list)):
            sum += a_list[finish]
            if sum == target:
                return True
    return False


# example of use
# print(sublist_sum([4, 9, 3, 1, 7, 2, 4], 13))


# the result is True because of the consecutive sublist [9, 3, 1]

def sublist_sum_rec(a_list, target):
    """ Same as sublist_sum, but recursive."""
    # print(a_list)
    sum = 0
    for x in range(len(a_list)):
        # For optimization; skips through list if a_list[x] > target.
        if a_list[x] > target:
            return sublist_sum_rec(a_list[x + 1:], target)
        else:
            sum += a_list[x]
            if sum == target:
                # print(a_list[:x + 1])
                return True
            elif sum > target:
                try:
                    return sublist_sum_rec(a_list[1:], target)
                except:
                    return False
    return False


print(sublist_sum_rec([4, 3, 1, 2, 3, 15, 9, 3, 1, 7, 2, 4], 14))

# Problem 3:

def prime_factors(n):
    ''' print the prime factorization of n'''
    while n > 1:
        candidate = 2
        while candidate <= n:
            if n % candidate == 0:
                print(candidate, " ", end="")  # this prints without starting a new line - very useful!
                n = n / candidate
            else:
                candidate += 1
    print("\n")


# example of use
# prime_factors(126)


# def prime_factors_rec(n):
#   you write this


# Problem 4:

def matching_parentheses(a_string):
    ''' determine if string a_string contains properly
       matched parentheses (i.e. each right parenthesis
       is matched with an earlier left parenthesis) '''
    left_parens = 0
    right_parens = 0
    for c in a_string:
        if c == '(':
            left_parens += 1
        elif c == ')':
            right_parens += 1
            if right_parens > left_parens:
                return False
    return (left_parens == right_parens)


# example of use
# print(matching_parentheses("abc((ef)gh(ij()k)lm((()n)opq())rst)uvw(xyz)"))

# def matching_parentheses_rec(a_string):
#   You write this