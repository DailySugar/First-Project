def equal_num_occurence(list_a, list_b, target):
    if len(list_a) != 0 and len(list_b) != 0:
        occur_a = 0
        occur_b = 0
        for x in list_a:
            if x == target:
                occur_a += 1
        for x in list_b:
            if x == target:
                occur_b += 1
        if occur_a == occur_b:
            return True
    return False


def test_equal_num_occurence():
    assert equal_num_occurence([],[],5) == False
    assert equal_num_occurence([5], [], 5) == False
    assert equal_num_occurence([3], [3,12], 3) == True
    assert equal_num_occurence([1.2,6,5], [5, 3.9,14,7], 3) == True
    assert equal_num_occurence([7.2,4,6,9.5,7.2], [-4,7.2,7.2], 7.2) == True


test_equal_num_occurence()