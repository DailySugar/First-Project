# October 16 2021

global puzzle
puzzle = [
    [6, 1, 4, 8],
    [2, 15, 3, 11],
    [5, 10, 14, 7],
    [13, 9, 0, 12]
]


def shift(start, shift):
    end = [x + y for x, y in zip(start, shift)]
    puzzle[start[0]][start[1]], puzzle[end[0]][end[1]] = puzzle[end[0]][end[1]], puzzle[start[0]][start[1]]
    print(puzzle)

def move_to(start, end):
    difference = [end[0] - start[0], end[1] - start[1]]
    if abs(difference[0]) == 1 or abs(difference[1]) == 1:
        shift(start, difference)


move_to([3,2],[3,1])

# def move(direction):
#     match direction:
#         case "left":
#         case "right":
#         case "up":
#         case "down":
