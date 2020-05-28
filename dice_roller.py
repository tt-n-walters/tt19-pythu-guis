import random
import tkinter as tk


def roll_dice(max=6):
    return random.randint(1, max)


def setup_window():
    window = tk.Tk()
    window.geometry("300x50")
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)

    number_ouput = tk.Label(window, text="Click the button to roll")
    button = tk.Button(window, text="Roll die")

    number_ouput.grid(row=1, column=1)
    button.grid(row=1, column=0)

    return window


if __name__ == "__main__":
    window = setup_window()
    window.mainloop()
