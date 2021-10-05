def smallestmultiple(num):
    "Finds smallest number that can be divided by all the numbers 'num' and below"
    output=num
    increment=num
    for x in range(1,num):
        while output % (num - x) > 0:
            output+=increment
        increment=output
    return output


print(smallestmultiple(20))