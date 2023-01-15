import tkinter as tk
import pyautogui
from PIL import Image, ImageGrab
import keyboard
import sys

from datetime import datetime


def take_screenshot():
    # Save the screenshot
    now = datetime.now()
    im = ImageGrab.grab(region)
    filename = now.strftime("screenshot_%Y-%m-%d_%H-%M-%S.jpg")
    print('Saving')
    im.save(filename)
    print('Saved')


def select_region():
    global region
    # Display the current mouse position
    print('Select the top-left corner of the region to capture, and press ctrl')
    pyautogui.displayMousePosition()
    coords1 = pyautogui.position()

    # Display the current mouse position
    print('Select the bottom-right corner of the region to capture, and press ctrl')
    pyautogui.displayMousePosition()
    coords2 = pyautogui.position()

    # Capture the region of the screen
    region = (coords1.x, coords1.y, coords2.x, coords2.y)


def on_closing():
    # Unregister the hotkey
    keyboard.unhook_all()
    root.destroy()


def register_extensions(id, extensions):
    print("register_extensions", extensions)
    for extension in extensions:
        Image.register_extension(id, extension)


def register_plugin():
    try:
        Image.register_extensions = register_extensions
        from PIL import PngImagePlugin
        print("PngImagePlugin import successful")
    except:
        print("PngImagePlugin import failed")
        raise


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Specify the key combination (ex: ctrl+alt+e)")
        exit(1)
    register_plugin()
    # Select the region at the start of the program
    select_region()

    keys = sys.argv[1]

    # Register the hotkey
    keyboard.add_hotkey(keys, take_screenshot)

    # Create a GUI window to keep the program running
    root = tk.Tk()
    root.title("Screenshot")
    root.geometry("200x200")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    label = tk.Label(root, text="Press " + keys + " to take a screenshot")
    label.pack()

    root.mainloop()
