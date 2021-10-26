'''
20211005

Robin Dawes

Demonstrates the recursive solution of the "Towers of Hanoi" puzzle, in which
the goal is to move 5 discs of increasing size from an initial state in which they
are stacked in order (largest at the bottom) on a peg labelled Peg 0, to a final
state in which they are stacked in the same order on a peg labelled Peg 2, using
a middle peg (Peg 1) to assist in the process.  The discs must be moved according
to these rules:
   1.  Only one disc can be moved at a time
   2.  A disc can only be moved from one peg to another peg.  They cannot be
        temporarily placed on the table, etc.
   3.  A larger disc can never be stacked on top of a smaller disc

The ultimate goal is to complete the transfer in as few moves as possible.

If you are not familiar with this puzzle you may want to try to solve it before
reading on!

The Recursive Approach:

The key to understanding the recursive solution is to visualize the situation just
before we move Disc 5 (the largest one) from Peg 0 to Peg 2.  At this point all the
other discs (1, 2, 3, 4) must be stacked on Peg 1.   And after we move Disc 5 to
Peg 2, the rest of the job consists of moving Discs 1 through 4 from Peg 1 to Peg 2.
So we can summarize the solution as:
      To move Discs 1 through 5 from Peg 0 to Peg 2:
            Move Discs 1 through 4 from Peg 0 to Peg 1
            Move Disc 5 from Peg 0 to Peg 2
            Move Discs 1 through 4 from Peg 1 to Peg 2

      And how do we move Discs 1 through 4 from Peg 0 to Peg 1?  Like this:
            Move Discs 1 through 3 from Peg 0 to Peg 2
            Move Disc 4 from Peg 0 to Peg 1
            Move Discs 1 through 3 from Peg 2 to Peg 1

You can see the recursive nature of this.  The code that follows has lots of
'''

pegs = [[], [], []]

pegs[0] = [5, 4, 3, 2, 1]

pegs[1] = []

pegs[2] = []


def show_pegs(indent=0):
    '''print the pegs on the console output stream'''
    for i in range(len(pegs)):
        print("\t" * indent, "Peg", i, ":", pegs[i])
    print("\n")


def move_one(i, j):
    '''move a disk from peg i to peg j if legal

       This function carries out the details of transferring a disc (just an integer)
       from one peg (a list) to another.

       The function checks to make sure the move is legal, though that is not
       really necessary since the algorithm never tries to break the rules.
    '''
    if pegs[i] != []:
        if pegs[j] == []:
            pegs[j] = [pegs[i][-1]]
            pegs[i] = pegs[i][:-1]
        elif pegs[i][-1] < pegs[j][-1]:
            pegs[j].append(pegs[i][-1])
            pegs[i] = pegs[i][:-1]


def move_some(source, target, how_many):
    '''move some number of discs from one peg to another

       This function implements the recursive solution as described above
    '''
    # print("\t"*(5 - how_many), "Moving", how_many, "disks from peg", source, "to peg", target)
    if how_many == 1:  # this is our base case
        print("\t" * (5 - how_many), "Moving 1 disk from peg", source, "to peg", target)
        move_one(source, target)
        show_pegs(indent=5 - how_many)  # the indent parameter is used to
        # make the output reflect the recursive
        # nesting of function calls
    else:
        print("\t" * (5 - how_many), "Moving", how_many, "disks from peg", source, "to peg", target)
        other_peg = (3 - (source + target)) % 3
        move_some(source, other_peg, how_many - 1)
        print("\t" * (5 - how_many), "Moving 1 disk from peg", source, "to peg", target)
        move_one(source, target)
        show_pegs(indent=5 - how_many)
        move_some(other_peg, target, how_many - 1)


move_some(0, 2, 5)

