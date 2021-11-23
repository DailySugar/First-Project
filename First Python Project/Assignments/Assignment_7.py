"""


"""

from pathlib import Path
import numpy as np
from random import randint

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


def k_means(animals_table, group_count = 7):
    """Generates initial groups and center values. Center values,
    and groups of animal indexes will be kept track of in the
    group dictionary."""
    animals_index_count = len(animals_table) - 1
    groups = {-1:set()}
    for x in range(group_count):
        temp_animal = randint(0, animals_index_count)
        groups[x] = [{temp_animal}, animals_table[temp_animal]]
        groups[-1].add(temp_animal)
    print("Initial Groups:", groups)
    return groups
    # for x in range(loops):
    #     for animal in animals_table:


def smallest(differences):
    """Returns the index of the smallest difference."""
    smallest = differences[0]
    for x in differences[1:]:
        if x < smallest:
            smallest = x
    # print(differences.index(smallest))
    return differences.index(smallest)


def manhattan_metric(animals_table, groups, loops = 10):
    for x in range(loops):
        for animal in range(len(animals_table)):
            if animal in groups[-1]:
                continue
            # print("animal_attributes:", animal_attributes)
            differences = []
            for compare in range(len(groups)):
                # print("compare:          ", compare)
                total_difference = 0
                for attribute in range(len(animals_table[animal])):
                    total_difference += abs(animals_table[animal][attribute] - groups[compare][1][attribute])
                differences.append(total_difference)
                # print("difference:",temp_differences)
            # print(differences)
            groups[smallest(differences)][0].add(animal)
        if x == 0:
            groups[-1] = {}
        print("Groups", groups)
        print("Elements:", len(groups[0][0]) + len(groups[1][0]) + len(groups[2][0]) + len(groups[3][0]) + len(groups[4][0]) + len(groups[5][0]) + len(
            groups[6][0]))
        for y in range(len(groups)):
            groups[y][0] = []
        print("Groups post-clear:", groups)


def main():
    groups = k_means(animals_table, 7)
    # print(manhattan_metric(animals_table, groups, 10))
    print(animals_table[10])
    print(animals_table[49])


main()
# print(k_means(animals_table))
# print(array(animals_table[0]))