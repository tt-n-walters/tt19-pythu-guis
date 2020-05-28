import random
import tkinter as tk


def roll_dice(max=6):
    return random.randint(1, max)


def setup_window():
    window = tk.Tk()

    number_ouput = tk.Label(window, text="Click the button to roll")
    button = tk.Button(window, text="Roll die")

    number_ouput.pack()
    button.pack()


if __name__ == "__main__":
    setup_window()
