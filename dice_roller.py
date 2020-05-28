import random
import tkinter as tk


# Core dice roll function
def roll_dice(max=6):
    return random.randint(1, max)


# Takes dice roll and updates display
def display_dice_roll():
    global number_output
    value = roll_dice()
    number_output["text"] = value


# Start dice rolling animation
def handle_click():
    for time in range(0, 501, 50):
        window.after(time, display_dice_roll)


def setup_window():
    window = tk.Tk()
    window.geometry("300x50")
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)

    number_args = {
        "text": "Click the button to roll",
        "font": ("Calibri", 16)
    }
    # Create a Frame to put the Label inside
    frame = tk.Frame(window, width=200, height=50)
    frame.pack_propagate(0)

    number_output = tk.Label(frame, **number_args)
    number_output.pack(fill=tk.BOTH, expand=tk.YES)
    button = tk.Button(window, text="Roll die", command=handle_click, font=("Calibri", 16))

    frame.grid(row=1, column=1)
    button.grid(row=1, column=0)

    return window, number_output


if __name__ == "__main__":
    window, number_output = setup_window()
    window.mainloop()
