"""
Pytest Practice

Created on Oct 1, 2021
Author: Alex Sun
Student Number: 20289530
CISC-121

I, Alex Sun, hereby declare that no plagiarism 
has been conducted in this assingment.
"""


# Third function:

def binary_string(n):
    '''parameter:
        n - integer
        
        returns a string of "0"s and "1"s giving the binary representation of n
        returns None if n is not an integer
    '''
    
    if type(n) is not int:
        return None
    else:
        if n == 0:
            return '0'
        else:
            negative = (n < 0)
            n = abs(n)
            bin_string = ''
            while n != 0:
                if n % 2 == 1:
                    bin_string = '1' + bin_string
                else:
                    bin_string = '0' + bin_string
                n = n // 2
            if negative:
                bin_string = '-' + bin_string
            return  bin_string  


def test_binary_string1():
    """
        Test non-integer
    """
    assert binary_string('1') == None
    
    
def test_binary_string2():
    """
        Test 1
    """
    assert binary_string(1) == "1"
    
    
def test_binary_string3():
    """
        Test 167
    """
    assert binary_string(167) == "10100111"