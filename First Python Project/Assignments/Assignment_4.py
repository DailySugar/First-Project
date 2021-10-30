"""
Created October 26, 2021
Alex Sun
20289530
CISC-121

Converting between recursive and non-recursive functions, and
optimizing recursive functions.
All work is mine, and any ideas "borrowed" are referenced above
the code.
"""


# Part 1

# For each of the non-recursive functions given here, create
# a recursive function that produces the same result

# Problem 1:

def exponent(x, y):  # y is a positive integer
    """ compute x^y, where y is a positive integer """
    result = x
    while y > 1:
        result = result * result
        if y % 2 == 1:
            result *= x
        y = y // 2
    return result

def exponent_rec(x, y):
    """ Exponentiation by squaring, thanks to Dawes for the
    original idea, and wikipedia.org/wiki/Exponentiation_by_squaring
    for a refresher. Also takes negative integers because I felt like it."""
    if y == 1:
        return x
    elif y == 0:
        return 1
    elif y < 0:
        return 1 / exponent_rec(x, -y)
    elif y % 2 == 0:
        return exponent_rec(x * x, y // 2)
    elif y % 2 == 1:
        return exponent_rec(x * x, y // 2) * x
    else:
        return -1


# Problem 2:

def sublist_sum(a_list, target):
    """ determine if list a_list has a consecutive sub-list that sums to target """
    for start in range(len(a_list)):
        sum = 0
        for finish in range(start, len(a_list)):
            sum += a_list[finish]
            if sum == target:
                return True
    return False


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


# Problem 3:

def prime_factors(n):
    """ print the prime factorization of n"""
    while n > 1:
        candidate = 2
        while candidate <= n:
            if n % candidate == 0:
                print(candidate, " ", end="")  # this prints without starting a new line - very useful!
                n = n / candidate
            else:
                candidate += 1
    print("\n")


def pfr(n, candidate):
    """ Recursive portion of prime_factors_rec."""
    if n != 1:
        if n % candidate == 0:
            print(candidate, " ", end="")
            pfr(n // candidate, candidate)
        else:
            pfr(n, candidate + 1)


def prime_factors_rec(n):
    """ Main calling function."""
    pfr(n, 2)


# Problem 4:

def matching_parentheses(a_string):
    """ determine if string a_string contains properly
       matched parentheses (i.e. each right parenthesis
       is matched with an earlier left parenthesis) """
    left_parens = 0
    right_parens = 0
    for c in a_string:
        if c == '(':
            left_parens += 1
        elif c == ')':
            right_parens += 1
            if right_parens > left_parens:
                return False
    return left_parens == right_parens


def mpr(a_string, index, left, right):
    """ Recursive portion of matching_parentheses_rec."""
    if len(a_string) <= index:
        return left == right
    elif a_string[index] == "(":
        return mpr(a_string, index + 1, left, right + 1)
    elif a_string[index] == ")":
        return mpr(a_string, index + 1, left + 1, right)
    else:
        return mpr(a_string, index + 1, left, right)


def matching_parentheses_rec(a_string):
    """ Main calling function."""
    return mpr(a_string, 0, 0, 0)


# Part 2:

# Each of these recursive functions is inefficient due to duplicated
# effort.  Improve them by storing the solutions to smaller problems that
# are needed repeatedly.

# Problem 5

def collatz_up_to_n(n):
    """ print the Collatz Sequence for each value from 1 to n """
    for i in range(n):
        collatz_rec(i + 1)


def collatz_rec(n):
    """ print the Collatz Sequence for a single integer """
    print(n, " ", end="")
    if n == 1:
        print("\n")
        return
    else:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_rec(n)


def better_collatz_rec(start, end, current_num, sequence_dict):
    """ This function stores the next part of the Collatz Sequence
    for all encountered integers to save time on calculating.
    For example, when the next int after 5 (16) is found,
    5 is stored as a reference to 16 in the dict for future
    reference."""
    if start == end:
        # print(sequence_dict)
        print()
        return
    else:
        if start == current_num:
            print("\n" + str(start), " ", end="")
        if current_num in sequence_dict:
            while current_num != 1:
                current_num = sequence_dict[current_num]
                print(current_num, " ", end="")
            return better_collatz_rec(start + 1, end, start + 1, sequence_dict)
        else:
            temp = current_num
            # Collatz Sequence algorithm
            if current_num % 2 == 0:
                current_num = current_num // 2
            else:
                current_num = 3 * current_num + 1
            # Add next part of Collatz Sequence
            sequence_dict[temp] = current_num
            print(current_num, " ", end="")
            return better_collatz_rec(start, end, current_num, sequence_dict)


def better_collatz_up_to_n(n):
    better_collatz_rec(1, n + 1, 1, {1:1})


# Problem 6

def count_routes(n):
    """ returns the number of different ways a robot can move forward a total of n metres, when the
        robot can only take steps that go forward either 2 metres or 3 metres. """
    if n <= 1:
        return 0
    elif n <= 3:
        return 1
    else:
        return count_routes(n - 2) + count_routes(n - 3)


path_dict = {}


def better_count_routes(n):
    """ This version stores all previously found paths in path_dict.
    The dictionary key is the length of the path."""
    try:
        return path_dict[n]
    except:
        if n <= 1:
            return 0
        elif n <= 3:
            return 1
        else:
            path_dict[n] = better_count_routes(n - 2) + better_count_routes(n - 3)
            return path_dict[n]


# Part 3

# Write non-recursive functions to produce the same results as these recursive functions

# Problem 7

def binary_search(a_list, target):
    """ returns the location of target in a_list if target is in a_list, returns -1 if target is not in a_list
        a_list must be sorted prior to calling this function
    """
    return binary_search_rec(a_list, target, 0, len(a_list) - 1)


def binary_search_rec(a_list, target, first, last):
    if first > last:
        return -1
    else:
        mid = (first + last) // 2
        if a_list[mid] == target:
            return mid
        elif a_list[mid] > target:
            return binary_search_rec(a_list, target, first, mid - 1)
        else:
            return binary_search_rec(a_list, target, mid + 1, last)


def bs(list, target):
    """ Not much to say here; it's just a non-recursive version of
    the above function."""
    for x in range(len(list)):
        if list[x] == target:
            return x
    return -1


# Problem 8

def gcd(a, b):
    """ returns the greatest common divisor of a and b, which must be positive integers """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd2(a, b):
    """ gcd, but looping instead of recursive."""
    if a % b == 0:
        return b
    elif b % a == 0:
         return a
    else:
        limit = 8 // 2
        while limit >= 1:
            if a % limit == 0 and b % limit == 0:
                return limit
            limit -= 1


def print_everything():
    """ Prints out all of the problem outputs.
    Easy to comment out."""

    print("Problem 1:")
    # print(exponent(3, 7))
    print(exponent_rec(3, 7), "\n")

    print("Problem 2:")
    # print(sublist_sum([4, 9, 3, 1, 7, 2, 4], 13))
    print(sublist_sum_rec([4, 9, 3, 1, 7, 2, 4], 13), "\n")

    print("Problem 3:")
    # prime_factors(126)
    prime_factors_rec(126)
    print("")

    print("\nProblem 4:")
    # print(matching_parentheses_rec("abc((ef)gh(ij()k)lm((()n)opq())rst)uvw(xyz)"))
    print(matching_parentheses("abc((ef)gh(ij()k)lm((()n)opq())rst)uvw(xyz)"))

    print("\nProblem 5:")
    # collatz_up_to_n(10)
    better_collatz_up_to_n(10)

    print("\nProblem 6:")
    # print(count_routes(10))
    print(better_count_routes(10))

    print("\nProblem 7:")
    # print(binary_search([4, 7, 12, 15, 23, 28, 33, 34, 35, 100, 5280, 5281], 100))
    print(bs([4, 7, 12, 15, 23, 28, 33, 34, 35, 100, 5280, 5281], 100))

    print("\nProblem 8:")
    # print(gcd(8, 20))
    print(gcd2(8, 20))

print_everything()