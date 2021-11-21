# October 28 2021
import time


pillars = 3
rings = 5
puzzle = []
for x in range(pillars):
    puzzle.insert(0, [])
for x in range(1, rings + 1):
    puzzle[0].append(x)


def move(start, end):
    if len(puzzle[start]) and (len(puzzle[end]) == 0 or puzzle[end][0] > puzzle[start][0]):
        puzzle[end].insert(0, puzzle[start][0])
        puzzle[start].pop(0)
        for x in puzzle:
            for y in reversed(x):
                print(y, end="   ")
            print()
        print("\n")
        time.sleep(0.5)
    else:
        print("ERROR: ILLEGAL MOVE ATTEMPTED")


def move_multiple(start, end, count):
    if count <= 1:
        move(start, end)
    else:
        move_multiple(start, pillars - start - end, count - 1)
        move(start, end)
        move_multiple(pillars - start - end, end, count - 1)


move_multiple(0, 2, 5)
# print(puzzle)