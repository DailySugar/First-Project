import timeit

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


start = timeit.default_timer()
print(gcd(23981203823801200000, 120912893740912830912749812704703808888800000000000))
stop = timeit.default_timer()
print(stop - start)