digits=5
num=(10**(digits)-1)**2

def get_palindrome(num):
    """Returns largest palindrome below or equal to given number"""
    palindrome=""
    if num<1:
        return None
    for index in range(len(str(num))//2):
        index2=len(str(num))-1-index
        increment=10**index
        #Flaw in algorithm here
        while str(num)[index]!=str(num)[index2]:
            num-=increment
    if(test_multiples(num, digits)):
        return num
    return get_palindrome(num-1)


def test_multiples(num, digits):
    """Returns true if the given number is a product of two numbers 
    with given digits"""
    start,end=10**(digits-1),10**(digits)-1
    for x in range(start,end):
        if num%x==0 and len(str(num//x))==digits:
            print(x,num/x)
            return True
        #print(x,num/x)
    return False

#print(test_multiples(100,2))
print(get_palindrome(num))
