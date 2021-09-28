num=20
output=num
increment=num

for x in range(1,num):
    while (output)%(num-x)!=0 or output//(num-x)%2!=0:
        output+=increment
    increment=output
    print(num-x,output)
print(output)