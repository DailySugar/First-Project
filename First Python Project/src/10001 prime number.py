#Created October 10
import math

primes = [2]


def is_prime(num):
    for x in primes:
        if num % x == 0:
            return False
        if x >= math.sqrt(num):
            return True
    return True


def next_prime(num):
    if num % 2 == 0:
        num += 1
    else:
        num += 2
    while not is_prime(num):
        num += 2
    primes.append(num)
    return num


place = 10001
ans = 2
for x in range(0, place - 1):
    ans = next_prime(ans)
print(ans)
