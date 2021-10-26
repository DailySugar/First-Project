'''
20211005

Robin Dawes
'''
import tkinter as tk

window = tk.Tk()
window.geometry("1200x800")

delay = 1600               # time in milliseconds between moves





pegs = [[],[],[]]
discs = 5

pegs[0] = [5,4,3,2,1]

pegs[1] = []

pegs[2] = []


disc_labels = []    # this list is used to keep track of old Labels that we destroy
                             # when we want to display a new position


def build_axes():
   '''The display of the discs on the pegs is done with the grid() placement.  The
      rows and columns are established with the Labels defined here.  These are
      placed in the left-hand column and the row below the rows where the discs
      will be shown.
   '''
   for i in range(discs):
      blank_label = tk.Label(window, text = "       ", font = (None, 20))
      blank_label.grid(row = i, column = 0)
   for peg in range(3):
      peg_label = tk.Label(window, text = "    "+str(peg)+"    ", font = (None, 22), bg = "black", fg = "white")
      peg_label.grid(row = discs + 1, column = peg + 1)

def display_pegs():
   global disc_labels    # We want to reset this to be empty, so it needs to be
                                    # assignable.

   # clear the display
   for dl in disc_labels:
         dl.destroy()

   disc_labels = []

   # show the new situation

   for p in range(len(pegs)):
      current_row = discs     # bottom row of the display grid
      for disc in pegs[p]:
         place = tk.Label(window, text = "   "+str(disc)+"   ", font = (None, 20))
         place.grid(row = current_row, column = p+1)
         disc_labels.append(place)    # save links to these labels so we can destroy
                                                      # them before the next display
         current_row -= 1



# the algorithm is the same as before

def show_pegs(indent = 0):
   '''print the pegs on the console output stream'''
   for i in range(len(pegs)):
      print("\t"* indent, "Peg", i, ":", pegs[i])
   print("\n")


def move_one(i,j):
   '''       move a disk from peg i to peg j if legal   '''
   if pegs[i] != []:
      if pegs[j] == []:
         pegs[j] = [pegs[i][-1]]
         pegs[i] = pegs[i][:-1]
      elif pegs[i][-1] < pegs[j][-1]:
         pegs[j].append(pegs[i][-1])
         pegs[i] = pegs[i][:-1]


def move_some(source, target, how_many):
   print("\t"*(5 - how_many), "Moving", how_many, "disks from peg", source, "to peg", target)
   if how_many > 1:
      other_peg = (3 - (source + target)) % 3
      move_some(source, other_peg, how_many - 1)
      move_one(source, target)
      window.after(delay)                       # wait a bit
      display_pegs()                                # rebuild the display
      window.update()                            # update the screen
      move_some(other_peg, target, how_many - 1)
   else:
      move_one(source, target)
      window.after(delay)
      display_pegs()
      window.update()

build_axes()                  # create the axes
display_pegs()               # build the initial state
window.update()            # update the screen

move_some(0, 2, 5)      # this initiates the process, which causes a lot of
                                    # tkinter operations which are queued up waiting to be
                                    # shown


window.mainloop()      # start tkinter display process