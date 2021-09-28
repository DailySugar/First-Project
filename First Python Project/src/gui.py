import tkinter as tk
#import and overwrite functions, or put * to import and overwrite all functions in tkinter
#from tkinter import *
import sys
from tkinter import font


window = tk.Tk()
window.title("test")
window.geometry("800x800")
window.defaultFont = font.nametofont("TkDefaultFont")

label_1=tk.Label(window,text="uwu")
entry_1=tk.Entry(window,width=10)
entry_2=tk.Entry(window,width=10)
text_1=tk.Text(window,height=5,width=30)


def button_1_clicked():
    try:
        x=str(entry_1.get())
    except ValueError:
        x=None
        
    try:
        y=str(entry_2.get())
    except ValueError:
        y=None
    text_1.delete(1.0,tk.END)
    text_1.insert(tk.END,x+y)

button_1 = tk.Button(window,text="Enter",command = button_1_clicked)
button_2 = tk.Button(window,text="Exit",command=sys.exit)

"""label_1.pack()
entry_1.pack()
text_1.pack()
button_1.pack()"""


label_1.grid(row=0,column=0)
entry_1.grid(row=1,column=0)
entry_2.grid(row=1,column=1)
text_1.grid(row=10,column=0)
button_1.grid(row=1,column=2)
button_2.grid(row=7,column=10)
window.mainloop()

