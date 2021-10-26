import tkinter as tk
#import and overwrite functions, or put * to import and overwrite all functions in tkinter
#from tkinter import *


window = tk.Tk()
window.title("test")
window.geometry("800x800")

label_1=tk.Label(window,text="uwu")
entry_1=tk.Entry(window,width=10)
entry_2=tk.Entry(window,width=10)
text_1=tk.Text(window,height=5,width=30)


def button_1_clicked():
    text="abc"
    key="z"
    while(len(text)>len(key)):
        key+=key
    output=""
    table="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for x in range(len(text)):
        output+=table[table.index(text[x])+table.index(key[x])]
    print("\nYour encrypted text is:",output)

button_1 = tk.Button(window,text="Enter",command = button_1_clicked)

"""label_1.pack()
entry_1.pack()
text_1.pack()
button_1.pack()"""


label_1.grid(row=0,column=0)
entry_1.grid(row=1,column=0)
entry_2.grid(row=2,column=0)
text_1.grid(row=1,column=1)
button_1.grid(row=2,column=2)
window.mainloop()

