'''
Created on Sep 17, 2021

@author: alexs
'''
import timeit
start = timeit.default_timer()


five,three,fifteen,x=0,0,0,1
num=1000

while 15*x<num:
    fifteen+=15*x
    five+=5*x
    three+=3*x
    x+=1
    #print(five,three)
while 5*x<num:
    five+=5*x
    three+=3*x
    x+=1
while 3*x<num:
    three+=3*x
    x+=1
    #print(three)

print(five+three-fifteen)


'''
Peter's code
value = 0

for num in range(1, 1000):
    if (num % 3 == 0 or num % 5 == 0):
        value += num

print(value)
'''


stop = timeit.default_timer()
print('Time: ', stop - start)  