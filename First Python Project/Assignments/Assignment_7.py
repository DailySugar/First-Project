"""
Created November 21, 2021
Alex Sun
20289530
CISC-121

Using the k-means clustering algorithm with the Manhattan or
Euclidean distance metric to group similar animals together.
"""

from pathlib import Path
import numpy as np
from random import randint
# Thanks to Q#5105517 on stack overflow for mentioning deepcopy
from copy import deepcopy
from math import sqrt

properties = 15
animals_dict = {}

animals_file = str(Path.home() / "Downloads/zoo_2.txt")
temp = 0
# Establish dictionary with animals and their row #
for line in (open(animals_file)).readlines()[1:]:
    animals_dict[temp] = line.split(" ")[0]
    temp += 1

animals_table = np.loadtxt(animals_file, dtype = int, skiprows=1, usecols=range(1,properties + 1))


def smallest(differences):
    """Returns the index of the smallest number in the list."""
    smallest = differences[0]
    for x in differences[1:]:
        if x < smallest:
            smallest = x
    # print(differences.index(smallest))
    return differences.index(smallest)


def manhattan(list1, list2):
    """Computes and returns the Manhattan Metric distance from
    two equal length lists."""
    total_difference = 0
    for x in range(len(list1)):
        total_difference += abs(list1[x] - list2[x])
    return total_difference


def euclidean(list1, list2):
    """Computes and returns the Euclidean distance from
    two equal length lists."""
    total_difference = 0
    for x in range(len(list1)):
        total_difference += (list1[x] - list2[x]) ** 2
    return sqrt(total_difference)


def cluster_stable(old_groups, new_groups):
    """Checks and returns true if the two groups have the same animals, and
    all attributes have a difference less than 0.1 between the two groups."""
    attributes = list(range(len(old_groups[0][1])))
    for group in old_groups.keys():
        if old_groups[group][0] != new_groups[group][0]:
            return False
        for attribute in attributes:
            if abs(old_groups[group][1][attribute] - new_groups[group][1][attribute]) > 0.1:
                return False
    return True


def k_means(animals_table, group_count = 7, distance_algorithm = manhattan):
    """Groups the animals in animals_table into different groups
    using the distance algorithm chosen (manhattan, or euclidean)"""
    max_iterations = 100
    animals_index_count = len(animals_table) - 1
    groups = {}
    initial_animals = set()
    animals = set(range(0, animals_index_count + 1))
    attributes_count = len(animals_table[0])

    # Build initial centres with their associated animals
    group_index = 0
    while len(initial_animals) < group_count:
        temp_animal = randint(0, animals_index_count)
        # print(group_index, temp_animal)
        if temp_animal not in initial_animals:
            groups[group_index] = [[temp_animal], animals_table[temp_animal]]
            initial_animals.add(temp_animal)
            group_index += 1
        else:
            continue
    # print("Initial Groups:", groups)

    # Exclude initial centre animals from first iteration, as they are already sorted
    unsorted = animals.difference(initial_animals)
    for x in range(max_iterations):
        # print("Loop:", x + 1)
        for animal in unsorted:
            differences = []
            # Determining the animal's group using the distance algorithm chosen
            for compare in range(group_count):
                differences.append(distance_algorithm(animals_table[animal], groups[compare][1]))
            #     print("Group:   ", compare)
            #     print("Animal:  ", animals_table[animal], animal, animals_dict[animal])
            #     print("Compare: ", groups[compare][1])
            #     print("Distance:", distance_algorithm(animals_table[animal], groups[compare][1]))
            # print("Chosen Group:", smallest(differences))
            groups[smallest(differences)][0].append(animal)
        # Updating centre values for each group
        for group_index in range(group_count):
            # print("Group:     ", group_index)
            group = groups[group_index][0]
            group_length = len(group)
            # Try and except in case group is empty
            try:
                updated_centre = animals_table[group[0]]
            except:
                continue
            for animal_index in range(1, group_length):
                # Credits to Q#14050824 on stack overflow for zip() to sum the contents of two lists
                updated_centre = [sum(attribute) for attribute in zip(*[updated_centre, animals_table[group[animal_index]]])]
            # print("Center Sum: ", updated_centre)
            # print("# Animals:  ", group_length, len(groups[group_index][0]))
            updated_centre = [attribute / group_length for attribute in updated_centre]
            # print("Updated:    ", updated_centre)
            groups[group_index][1] = updated_centre
        # print("Group After:", groups)

        # After first iteration, include the initial animals
        if x == 0:
            unsorted = animals
        else:
            # Start checking for stability after first iteration
            # Stop looping if clustering algorithm has reached stability
            if cluster_stable(old_groups, groups):
                print("Stop looping at", x + 1)
                # print(groups)
                # print(old_groups)
                return groups
        old_groups = deepcopy(groups)
        for group in range(group_count):
            groups[group][0] = []
    return old_groups


def main():
    # groups = k_means(animals_table, distance_algorithm = euclidean)
    groups = k_means(animals_table, distance_algorithm = manhattan)
    for group in range(len(groups)):
        print("Group", group + 1, ":", end = " ")
        for animal in groups[group][0]:
            print(animals_dict[animal], end = " ")
        print()


main()
# print(k_means(animals_table))
# print(array(animals_table[0]))