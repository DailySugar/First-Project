def next_palindrome(num):
    length = len(str(num))
    for x in range(length // 2):
        while str(num)[x] != str(num)[length - x - 1]:
            num -= 10 ** x
    return num


def largest_palindrome(digits, num = 0, num2 = 0):
    if num2 == 0:
        num2 = int("9" * digits)
        num = num2 ** 2
    
    num = next_palindrome(num)
    for x in range(num2, 10 ** (digits - 1) - 1, -1):
        if num % x == 0 and num // x // (10 ** (digits - 1)) in range(1, 10):
            print(num % x)
            print(x // (10 ** (digits - 1)))
            print(x, num // x)
            return num
    if num % 10 ** (len(str(num)) - 1) == 1:
        return largest_palindrome(digits, num - 2, num2)
    else: 
        return largest_palindrome(digits, num - 1, num2)


#print(next_palindrome(997798))
print(largest_palindrome(3, 10001, 999))