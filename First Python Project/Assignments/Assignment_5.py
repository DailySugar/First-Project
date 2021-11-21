"""
Created November 2, 2021
Alex Sun
20289530
CISC-121

Creating a Radix sort and Quicksort function
"""
from random import randint
from math import floor
from timeit import default_timer


def generate_list(min, max, size):
    """ Generates a list of random ints from min to max.
    # of ints generated determined by size."""
    list = []
    for x in range(size):
        list.append(floor(randint(min, max)))
    return list


def radix_sort(list):
    """ Iteratively sorts using the radix sort method and dictionaries."""
    return_list = []
    digits = 1
    while list:
        # Empty dictionary every loop
        digit_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        for num in list:
            temp_num = num // digits
            # If num doesn't have digit, remove from loop (done sorting)
            if temp_num == 0:
                return_list.append(num)
            # Otherwise add to dictionary (keep sorting)
            else:
                digit_dict[temp_num % 10].append(num)
        # Replace list with dictionary contents
        list = []
        for x in range(0, 10):
            list += digit_dict[x]
        digits *= 10
    return return_list


def quick_sort_rec(list, left, right):
    """ Recursive portion of quick_sort()."""
    # Done sorting
    if left >= right:
        return list
    # Temporary values
    from_left = left
    from_right = right
    pivot = list[left]
    while from_left <= from_right:
        # Converge left and right
        while from_left <= from_right and list[from_left] <= pivot:
            from_left += 1
        while from_left <= from_right and list[from_right] >= pivot:
            from_right -= 1
        # Swap ints at left and right if left > pivot > right
        if from_left < from_right:
            list[from_left], list[from_right] = list[from_right], list[from_left]
        else:
            # Left and right have converged, so move pivot in between sorted ints.
            list.insert(from_left - 1, list.pop(left))
    # Sort ints before and after pivot
    quick_sort_rec(list, left, from_left - 2)
    quick_sort_rec(list, from_left, right)
    return list


def quick_sort(list):
    """ Main calling function for quicksort."""
    return(quick_sort_rec(list, 0, len(list) - 1))


if __name__ == "__main__":
    for x in range(100):
        test1 = generate_list(100000, 999999, 100)
        test2 = test1.copy()
        if not quick_sort(test1) == radix_sort(test2):
            print("Failed Check")
    print("Passed Check")

    time1 = 0
    time2 = 0
    total_time1 = 0
    total_time2 = 0
    runs = 100
    radix_sort_faster = 0
    for x in range(runs):
        test3 = generate_list(100000, 999999, 10000)
        test4 = test3.copy()

        start = default_timer()
        test3 = radix_sort(test3)
        time1 = default_timer() - start
        # print(stop - start)
        total_time1 += time1

        start = default_timer()
        test4 = quick_sort(test4)
        time2 = default_timer() - start
        # print(stop - start)
        total_time2 += time2

        if time1 < time2:
            radix_sort_faster += 1

    print("Average time for radix sort:", total_time1 / runs)
    print("Average time for quick sort:", total_time2 / runs)
    print("Radix sort was faster than quick sort", radix_sort_faster / runs * 100, "% of the time")

""" Over 300 runs, radix sort was faster 100% of the time, and 
had an average time of 6.2629 milliseconds, while quick sort had an average 
of 31.2338 milliseconds. Needless to say, my radix sort was much faster 
than my quick sort algorithm, which probably needs more optimization, 
but I'm not sure how to go about doing that."""


