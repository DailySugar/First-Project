def is_reverse(string_1, string_2):
    """
    Returns True if string_1 is the reversal
    of string_2, else returns False.
    """
    length = len(string_1)
    if length == len(string_2) and length != 0:
        for x in range(length):
            if string_1[x] != string_2[length - x - 1]:
                return False
        return True
    return False

def test_is_reverse():
    """Testing is_reverse function."""
    assert is_reverse("","") == False
    assert is_reverse("abc", "") == False
    assert is_reverse("abc", "bca") == False
    assert is_reverse("abc", "cba") == True
    assert is_reverse("a", "a") == True

test_is_reverse()