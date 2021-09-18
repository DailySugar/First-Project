'''
Created on Sep 17, 2021

@author: alexs
'''

import timeit
start = timeit.default_timer()


num=4000000
prev=1
curr=2
ans=0

while curr<num:
    if curr%2==0:
        ans+=curr
        print(curr)
    prev+=curr
    curr,prev=prev,curr
print(ans)

stop = timeit.default_timer()
print(stop-start)