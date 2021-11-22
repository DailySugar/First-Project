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
    groups = {}
    animals_index_count = len(animals_table) - 1
    groups["unsorted"] = list(animals_dict.keys())
    for x in range(group_count):
        temp_animal = randint(0, animals_index_count)
        groups[x] = [[temp_animal], animals_table[temp_animal]]
        groups["unsorted"].remove(temp_animal)
    print(groups)
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
            # print("animal_attributes:", animal_attributes)
            differences = []
            for compare in centers:
                # print("compare:          ", compare)
                total_difference = 0
                for attribute in range(len(animals_table[animal])):
                    total_difference += abs(animals_table[animal][attribute] - compare[attribute])
                differences.append(total_difference)
                # print("difference:",temp_differences)
            # print(differences)
            try:
                groups[smallest(differences)].append(animal)
            except:
                groups[smallest(differences)] = [animal]
        print(groups)
        print(len(groups[0]) + len(groups[1]) + len(groups[2]) + len(groups[3]) + len(groups[4]) + len(groups[5]) + len(
            groups[6]))
        for y in range(len(groups)):
            groups[y] = []
        print(groups)


def main():
    groups = k_means(animals_table, 7)
    print(manhattan_metric(animals_table, groups, 10))


main()
# print(k_means(animals_table))
# print(array(animals_table[0]))