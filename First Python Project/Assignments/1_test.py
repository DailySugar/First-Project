x = [1,2,3,4,5,6,7,8,9]

for y in iter(x):
    if y == 3:
        next(iter(x), None)
        print(y)
    else:
        print(y)