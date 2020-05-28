from tkinter import *


window = Tk()
window.geometry("400x300")

my_label = Label(window, text="Hello world!", fg="yellow", bg="black")
my_label.pack()


window.mainloop()
