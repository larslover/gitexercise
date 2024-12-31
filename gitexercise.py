from tkinter import *

root = Tk()
root.geometry("600x600+10+10")
name = Label(text="hello there")

name.pack()
name = Label(text="the second change")

name.pack()
name = Label(text="the third change")

name.pack()
name = Label(text="this is first change")
name.pack()
print("this is code running")
root.mainloop()