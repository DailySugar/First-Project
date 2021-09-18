#Declare variables
a=30
b=105
#So we don't have to deal with temp variables:
starterstring="The product of {0} and {1} is".format(a,b)
ans=0

while(a!=1):
    if(a%2==1):
        ans+=b
    a//=2
    b*=2

#Since the while loop cuts off before the last addition to the answer, another one needs to be put in after    
ans+=b

print(starterstring,ans)