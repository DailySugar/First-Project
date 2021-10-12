#Oct 12 2021
import math


#Not used in solution
def e_primes(num, sieve = 2, primes_list = []):
    """Finds primes up to num using Eratosthene's method."""
    if sieve == 2:
        primes_list.insert(0, 2)
        for x in range(3, num + 1, 2):
            primes_list.insert(len(primes_list), x)
    elif sieve > math.sqrt(num):
        return primes_list
    #print(primes_list[0:100])
    sieve = primes_list[primes_list.index(sieve) + 1]
    for x in primes_list[primes_list.index(sieve) + 1:]:
        if x % sieve == 0:
            primes_list.remove(x)
    return e_primes(num, sieve, primes_list)


def check_prime(num, primes):
    """Adds number to the end of primes and returns if it's prime."""
    for y in primes:
        if num % y == 0:
            return primes
        elif y >= math.sqrt(num):
            primes.append(num)
            return primes
    primes.append(num)
    return primes


def primes(num):
    """Returns all prime numbers num and below."""
    primes = []
    for x in range(2, num + 1):
        check_prime(x, primes)
    return primes


sum = 0
for x in primes(2000000):
    sum += x
print(sum)