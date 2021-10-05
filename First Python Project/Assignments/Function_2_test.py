"""
Pytest Practice

Created on Oct 1, 2021
Author: Alex Sun
Student Number: 20289530
CISC-121

is_plagiarism() == False
"""


# Second function:   

def primes_up_to_n(n):
    '''parameter :
        n - integer
        
        returns a list of all primes <= n
        returns None if n is not an integer
    '''
    if type(n) is not int:
        return None
    else:
        list_of_primes = []
        for potential_prime in range(2,n+1):
            #print("potential prime",potential_prime)
            could_be_prime = True
            done = False
            possible_divisor = 2
            while could_be_prime and possible_divisor < potential_prime:
                #print("\tpossible divisor",possible_divisor)
                if potential_prime % possible_divisor == 0:
                    could_be_prime = False
                    is_prime = False
                else:
                    possible_divisor += 1
        
            if possible_divisor == potential_prime:
                list_of_primes.append(potential_prime)
        
        return list_of_primes


def test_primes_up_to_n1():
    """
        Test non-integer
    """
    assert primes_up_to_n('100') == None
    

def test_primes_up_to_n2():
    """
        Test 1
    """
    assert primes_up_to_n(1) == []
    
    
def test_primes_up_to_n3():
    """
        Test 100
    """
    assert primes_up_to_n(100) == [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]