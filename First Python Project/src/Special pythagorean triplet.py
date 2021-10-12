#October 11
import math

squares = []
triplets = []
#Find pythagorean triplets up to 1000
def main():
    for x in range(1, 1000):
        squares.insert(len(squares), x ** 2)
        for y in range(0, len(squares)):
            if squares[y] >= x ** 2:
                break
            else:
                for z in squares[y+1:]:
                    if squares[y] + z == x ** 2:
                        if math.sqrt(squares[y]) + math.sqrt(z) + x == 1000:
                            print(math.sqrt(squares[y]), math.sqrt(z), x)
                            return
                        #triplets.insert(len(triplets), (squares[y], z, x ** 2))
main()
print(triplets)