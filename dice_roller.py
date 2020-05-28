import random
import tkinter as tk


def roll_dice(max=6):
    return random.randint(1, max)


def display_dice_roll():
    global number_output
    value = roll_dice()
    number_output["text"] = value


def handle_click():
    for time in range(0, 501, 50):
        window.after(time, display_dice_roll)


def setup_window():
    window = tk.Tk()
    window.geometry("300x50")
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)

    number_output = tk.Label(
        window,
        text="Click the button to roll",
        font=("Calibri", 16)
    )
    button = tk.Button(window, text="Roll die", command=handle_click, font=("Calibri", 16))

    number_output.grid(row=1, column=1)
    button.grid(row=1, column=0)

    return window, number_output


if __name__ == "__main__":
    window, number_output = setup_window()
    window.mainloop()
