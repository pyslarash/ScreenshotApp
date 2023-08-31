import os
import time
import pyautogui
import tkinter as tk # Importing a module as a variable

# Check if screenshots directory exists; if not - create it
def create_screenshots_directory():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

# The screenshot functionality
def screenshot():
    # Minimize the app window
    root.iconify()
    # Create the "screenshots" directory if it doesn't exist
    create_screenshots_directory()
    # Create a random name using current time
    name = int(round(time.time()*1000))
    # the number will be .png
    name = 'screenshots\{}.png'.format(name)
    # Pause for a brief moment to allow the window to minimize
    time.sleep(1)
    # Save as test.png
    img = pyautogui.screenshot(name)
    # Restore the app window
    root.deiconify()
    # Show the screenshot
    img.show()

# Creating a frame
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# This button takes a screenshot
button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)

button.pack(side=tk.LEFT) # The button is at the left of the screen

# This button closes the app
close = tk.Button(
    frame,
    text="Close",
    command=quit
)

close.pack(side=tk.LEFT) # The button is at the left of the screen

root.mainloop()