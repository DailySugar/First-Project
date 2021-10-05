"""
Pytest Practice

Created on Oct 1, 2021
Author: Alex Sun
Student Number: 20289530
CISC-121

Ctrl+C + Ctrl+V != True
"""


# First function:

def independent(list_a, list_b):
    '''
        We can say that two lists are independent if no value occupies the
        same position in both lists.  Independent lists are not
        required to have the same length.
        
            For example, [1,2] and [2,1,3] are independent, and
            [1,2,3]  and [4,2,'a'] are not independent.
        
        Parameters:
            list_a and list_b must be lists
        
        Returns True if list_a and list_b are independent, and
        returns False if they are not
    '''
    if type(list_a) is not list  or type(list_b) is not list:
        return False
    else:
        min_length = min(len(list_a), len(list_b))
        for i in range(min_length):
            if list_a[i] == list_b[i]:
                return False
    return True


def test_independent1():
    """
        Test for cases where there are same values, but not in 
        the same positions.
    """
    assert independent([1,2,3,4], [4,3,2,1]) == True
    

def test_independent2():
    """
        Test for cases where there are integers >9
    """
    assert independent([12,34], [1,2,3,4]) == True


def test_independent3():
    """
        Test for same values same positions
    """
    assert independent([50,23,7,17], [106,230,8,17]) == False
    
def test_independent4():
    """
        Test for differently sized lists
    """
    assert independent([100,200,300,400], [1000,2000,80,400,2,5,7,8,1,2,4,6,8,9]) == False