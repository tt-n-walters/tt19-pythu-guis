from tkinter import *


window = Tk()
window.geometry("400x300")

my_label = Label(window, text="Hello world!", fg="yellow", bg="black")
my_label.pack()

def button_click():
    print("Oh my! You clicked on the button!")

my_button = Button(window, text="Click me!", command=button_click)
my_button.pack()

window.mainloop()
