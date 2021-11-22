from timeit import default_timer

list = []
for x in range(10000000):
    list.append(x)

start = default_timer()
largest = list[0]
for x in list[1:]:
    if x > largest:
        largest = x
print(list.index(largest))
stop = default_timer()
print(start - stop)

start = default_timer()
largest = list[0]
largest_index = 0
for x in range(1, len(list)):
    if list[x] > largest:
        largest = list[x]
        largest_index = x
print(largest)
stop = default_timer()
print(start - stop)

start = default_timer()
largest = 0
for x in range(1, len(list)):
    if list[x] > list[largest]:
        largest = x
print(largest)
stop = default_timer()
print(start - stop)

