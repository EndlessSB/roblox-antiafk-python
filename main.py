import random
import time
from pynput.mouse import Controller
from pynput.keyboard import Controller as KeyboardController, Key, Listener

# Initialize the keyboard controller
keyboard = KeyboardController()

# Set the time range for holding the keys
MIN_TIME = 8
MAX_TIME = 12

# Initialize a flag for enabling/disabling the script
enabled = False

# Define the keys to press
keys = ['w', 'a', 's', 'd']

# Function to press and hold a key for a random duration
def press_key(key):
    keyboard.press(key)
    hold_time = random.randint(MIN_TIME, MAX_TIME)
    time.sleep(hold_time)
    keyboard.release(key)

# Function to handle the key press and release
def toggle_script(key):
    global enabled
    if key == Key.ctrl_l:
        # Pressing Ctrl + J toggles the script
        enabled = not enabled
        if enabled:
            print("Script Enabled: Random key presses started.")
        else:
            print("Script Disabled: Random key presses stopped.")

# Function to handle the random key press loop
def random_key_presses():
    while True:
        if enabled:
            key = random.choice(keys)
            press_key(key)
            time.sleep(random.uniform(1, 3))  # Delay between key presses

# Listener to detect key presses
def on_press(key):
    toggle_script(key)

# Start the listener to detect keyboard events
listener = Listener(on_press=on_press)
listener.start()

# Run the random key press function
random_key_presses()
