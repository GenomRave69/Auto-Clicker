import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox

# Global variables for managing clicking
clicking = False
click_interval = 0.1  # Interval between clicks in seconds
click_count = 0  # Counter for limiting the number of clicks

# Function for automatic clicking
def click_mouse():
    global click_count
    count = 0
    while clicking:
        pyautogui.click(button=mouse_button.get().lower())
        time.sleep(click_interval)
        count += 1
        if click_type.get() == "Repeat" and count >= int(repeat_count.get()):
            stop_clicking()
            break

# Start clicking
def start_clicking():
    global clicking, click_interval
    try:
        click_interval = (int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get()) + int(milliseconds.get()) / 1000)
        if click_interval <= 0:
            raise ValueError
        clicking = True
        threading.Thread(target=click_mouse).start()
    except ValueError:
        messagebox.showerror("Error", "Invalid click interval!")

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

# Fields for click interval
tk.Label(root, text="Click Interval").grid(row=0, column=0, columnspan=4)
hours = tk.Entry(root, width=5)
hours.grid(row=1, column=0)
hours.insert(0, "0")
tk.Label(root, text="hours").grid(row=1, column=1)

minutes = tk.Entry(root, width=5)
minutes.grid(row=1, column=2)
minutes.insert(0, "0")
tk.Label(root, text="mins").grid(row=1, column=3)

seconds = tk.Entry(root, width=5)
seconds.grid(row=2, column=0)
seconds.insert(0, "0")
tk.Label(root, text="secs").grid(row=2, column=1)

milliseconds = tk.Entry(root, width=5)
milliseconds.grid(row=2, column=2)
milliseconds.insert(0, "100")
tk.Label(root, text="ms").grid(row=2, column=3)

# Mouse button selection
tk.Label(root, text="Mouse Button").grid(row=3, column=0, columnspan=2)
mouse_button = tk.StringVar(value="Left")
tk.OptionMenu(root, mouse_button, "Left", "Right", "Middle").grid(row=3, column=2, columnspan=2)

# Click type
tk.Label(root, text="Click Type").grid(row=4, column=0, columnspan=2)
click_type = tk.StringVar(value="Single")
tk.OptionMenu(root, click_type, "Single", "Double").grid(row=4, column=2, columnspan=2)

# Repeat options
tk.Label(root, text="Click Repeat").grid(row=5, column=0, columnspan=2)
repeat_count = tk.Entry(root, width=5)
repeat_count.grid(row=5, column=2)
repeat_count.insert(0, "1")

repeat_mode = tk.StringVar(value="Repeat until stopped")
tk.Radiobutton(root, text="Repeat N times", variable=repeat_mode, value="Repeat").grid(row=6, column=0, columnspan=2)
tk.Radiobutton(root, text="Repeat until stopped", variable=repeat_mode, value="Repeat until stopped").grid(row=6, column=2, columnspan=2)

# Cursor position
tk.Label(root, text="Cursor Position").grid(row=7, column=0, columnspan=2)
x_pos = tk.IntVar(value=0)
y_pos = tk.IntVar(value=0)
tk.Radiobutton(root, text="Current position", variable=x_pos, value=-1).grid(row=8, column=0, columnspan=2)
tk.Radiobutton(root, text="Pick position", variable=x_pos, value=1).grid(row=8, column=2, columnspan=2)

# X and Y coordinate fields
tk.Label(root, text="X:").grid(row=9, column=0)
tk.Entry(root, textvariable=x_pos, width=10).grid(row=9, column=1)
tk.Label(root, text="Y:").grid(row=9, column=2)
tk.Entry(root, textvariable=y_pos, width=10).grid(row=9, column=3)

# Control buttons
start_button = tk.Button(root, text="Start (F6)", command=start_clicking, width=20)
start_button.grid(row=10, column=0, columnspan=2)

stop_button = tk.Button(root, text="Stop (F6)", command=stop_clicking, width=20)
stop_button.grid(row=10, column=2, columnspan=2)

# Pick location button
pick_button = tk.Button(root, text="Pick location", command=pick_location, width=20)
pick_button.grid(row=11, column=0, columnspan=4)

# Start the main GUI loop
root.mainloop()
