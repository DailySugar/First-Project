# 20210905
# R. Dawes

# Question:  What needs to be fixed in this program?

from tkinter import *

window = Tk()
window.title("Simple Adder")
window.geometry("550x300")

# get the first number
get_num1_label = Label(window,text="Enter an integer")
num1 = Entry(window, width = 10)


# get the second number
get_num2_label = Label(window,text="Enter another integer")
num2 = Entry(window, width = 10)

# place these things on the window
get_num1_label.grid(column = 0,row = 0)
num1.grid(column = 1, row = 0)
get_num2_label.grid(column = 0, row = 1)
num2.grid(column = 1, row = 1)

def clicked():
   
    x = num1.get()
    y = num2.get()
    sum = int(x) + int(y)
    sum_text = Text(window,height=3, width = 30)
    sum_text.insert(END,"\n   The sum is "+str(sum))
    sum_text.grid(column = 1, row = 4)
   
add_them_button = Button(window, text = "Add the numbers", command = clicked)

add_them_button.grid(column = 3, row = 0)


   
window.mainloop()
