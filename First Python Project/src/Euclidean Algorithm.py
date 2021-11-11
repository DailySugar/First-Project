import timeit

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


start = timeit.default_timer()
print(gcd(62615533, 7907))
stop = timeit.default_timer()
print(stop - start)