"""


"""

from pathlib import Path
import numpy as np
from random import randint
from copy import deepcopy
# Thanks to Q#5105517 on stack overflow for mentioning this

properties = 15
animals_dict = {}

animals_file = str(Path.home() / "Downloads/zoo_2.txt")
temp = 0
# Establish dictionary with animals and their row #
for line in (open(animals_file)).readlines()[1:]:
    animals_dict[temp] = line.split(" ")[0]
    temp += 1

animals_table = np.loadtxt(animals_file, dtype = int, skiprows=1, usecols=range(1,properties + 1))

# print(animals_dict)


def smallest(differences):
    """Returns the index of the smallest difference."""
    smallest = differences[0]
    for x in differences[1:]:
        if x < smallest:
            smallest = x
    # print(differences.index(smallest))
    return differences.index(smallest)


def manhattan(list1, list2):
    total_difference = 0
    for x in range(len(list1)):
        total_difference += abs(list1[x] - list2[x])
    return total_difference


def cluster_stable(old, new):
    for x in range(len(old)):
        if abs(old[x] - new[x]) > 0.1:
            return False
    return True


def k_means(animals_table, group_count = 7, loops = 7, distance_algorithm = manhattan):
    max_iterations = 100
    animals_index_count = len(animals_table) - 1
    groups = {}
    initial_animals = set()
    animals = set(range(0, animals_index_count + 1))
    attributes_count = len(animals_table[0])

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
    # print("Initial Groups:", initial_animals)

    unsorted = animals.difference(initial_animals)
    for x in range(max_iterations):
        # print("Loop:", x + 1)
        for animal in unsorted:
            differences = []
            for compare in range(group_count):
                differences.append(distance_algorithm(animals_table[animal], groups[compare][1]))
            groups[smallest(differences)][0].append(animal)
        for group_index in range(group_count):
            group = groups[group_index][0]
            group_length = len(group)
            try:
                updated_centre = animals_table[group[0]]
            except:
                continue
            # if group_index == 0:
            #     # print("Animals in group", group_index, ":", group_length)
            #     print(groups[0])
            for animal_index in range(1, group_length):
                # Credits to Q#14050824 on stack overflow for zip() to sum the contents of two lists
                updated_centre = [sum(attribute) for attribute in zip(*[updated_centre, animals_table[group[animal_index]]])]
            # if group_index == 0: print(updated_centre)
            updated_centre = [attribute / group_length for attribute in updated_centre]
            # if group_index == 0: print(updated_centre)
            groups[group_index][1] = updated_centre

        # After first iteration, include the initial animals
        if x == 0:
            unsorted = animals
        else:
            loop_again = 0
            for group in range(group_count):
                if old_groups[group] != groups[group]:
                    loop_again = 1
                    break
                if not cluster_stable(old_groups[group][1], groups[group][1]):
                    loop_again = 1
                    break
            if loop_again == 0:
                print("Stop looping at", x + 1)
                # print(groups)
                # print(old_groups)
                return groups
        old_groups = deepcopy(groups)
        if x < max_iterations - 1:
            for group in range(group_count):
                groups[group][0] = []
    return groups

def main():
    groups = k_means(animals_table, distance_algorithm = manhattan)
    for group in range(len(groups)):
        print("Group", group + 1, ":", end = " ")
        for animal in groups[group][0]:
            print(animals_dict[animal], end = " ")
        print()
    # print(animals_table[10])
    # print(animals_table[49])


main()
# print(k_means(animals_table))
# print(array(animals_table[0]))