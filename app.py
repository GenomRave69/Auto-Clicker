import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox
import random

# Global variables for managing clicking
clicking = False
click_count = 0  # Counter for limiting the number of clicks

# Function for automatic clicking with random interval
def click_mouse():
    global click_count
    count = 0
    while clicking:
        pyautogui.click(button=mouse_button.get().lower())
        # Use a random interval between clicks
        random_interval = random.uniform(float(min_interval.get()), float(max_interval.get()))
        time.sleep(random_interval)
        count += 1
        if repeat_mode.get() == "Repeat" and count >= int(repeat_count.get()):
            stop_clicking()
            break

# Start clicking
def start_clicking():
    global clicking
    try:
        if float(min_interval.get()) <= 0 or float(max_interval.get()) <= 0 or float(min_interval.get()) > float(max_interval.get()):
            raise ValueError
        clicking = True
        threading.Thread(target=click_mouse).start()
    except ValueError:
        messagebox.showerror("Error", "Invalid interval values!")

# Stop clicking
def stop_clicking():
    global clicking
    clicking = False

# Pick click location
def pick_location():
    root.withdraw()  # Hide the window for location selection
    time.sleep(2)  # Delay to pick location
    x, y = pyautogui.position()  # Get the current cursor position
    x_pos.set(x)
    y_pos.set(y)
    root.deiconify()  # Show the window again after picking position

# GUI with tkinter
root = tk.Tk()
root.title("Auto Clicker")

# Fields for random click interval
tk.Label(root, text="Min Interval (sec)").grid(row=0, column=0, columnspan=2)
min_interval = tk.Entry(root, width=10)
min_interval.grid(row=0, column=2)
min_interval.insert(0, "0.1")

tk.Label(root, text="Max Interval (sec)").grid(row=1, column=0, columnspan=2)
max_interval = tk.Entry(root, width=10)
max_interval.grid(row=1, column=2)
max_interval.insert(0, "1.0")

# Mouse button selection
tk.Label(root, text="Mouse Button").grid(row=2, column=0, columnspan=2)
mouse_button = tk.StringVar(value="Left")
tk.OptionMenu(root, mouse_button, "Left", "Right", "Middle").grid(row=2, column=2, columnspan=2)

# Click type
tk.Label(root, text="Click Type").grid(row=3, column=0, columnspan=2)
click_type = tk.StringVar(value="Single")
tk.OptionMenu(root, click_type, "Single", "Double").grid(row=3, column=2, columnspan=2)

# Repeat options
tk.Label(root, text="Click Repeat").grid(row=4, column=0, columnspan=2)
repeat_count = tk.Entry(root, width=5)
repeat_count.grid(row=4, column=2)
repeat_count.insert(0, "1")

repeat_mode = tk.StringVar(value="Repeat until stopped")
tk.Radiobutton(root, text="Repeat N times", variable=repeat_mode, value="Repeat").grid(row=5, column=0, columnspan=2)
tk.Radiobutton(root, text="Repeat until stopped", variable=repeat_mode, value="Repeat until stopped").grid(row=5, column=2, columnspan=2)

# Cursor position
tk.Label(root, text="Cursor Position").grid(row=6, column=0, columnspan=2)
x_pos = tk.IntVar(value=0)
y_pos = tk.IntVar(value=0)
tk.Radiobutton(root, text="Current position", variable=x_pos, value=-1).grid(row=7, column=0, columnspan=2)
tk.Radiobutton(root, text="Pick position", variable=x_pos, value=1).grid(row=7, column=2, columnspan=2)

# X and Y coordinate fields
tk.Label(root, text="X:").grid(row=8, column=0)
tk.Entry(root, textvariable=x_pos, width=10).grid(row=8, column=1)
tk.Label(root, text="Y:").grid(row=8, column=2)
tk.Entry(root, textvariable=y_pos, width=10).grid(row=8, column=3)

# Control buttons
start_button = tk.Button(root, text="Start (F6)", command=start_clicking, width=20)
start_button.grid(row=9, column=0, columnspan=2)

stop_button = tk.Button(root, text="Stop (F6)", command=stop_clicking, width=20)
stop_button.grid(row=9, column=2, columnspan=2)

# Pick location button
pick_button = tk.Button(root, text="Pick location", command=pick_location, width=20)
pick_button.grid(row=10, column=0, columnspan=4)

# Start the main GUI loop
root.mainloop()
