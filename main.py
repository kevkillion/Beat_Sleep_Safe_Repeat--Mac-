
import pyautogui
import time

# Activate FAILSAFE to abort program by moving cursor to (0,0) upper left corner of screen
pyautogui.FAILSAFE = True

pyautogui.moveTo(50,100) # Set mouse cursor start position

# Function to move mouse cursor 10 units left and right
def move_mouse():
    pyautogui.moveRel(10, 0)
    time.sleep(2)
    pyautogui.moveRel(-10, 0)

# Function to switch screens right Mac keyboard
def switch_screen_right():
    pyautogui.hotkey('ctrl', 'right')
    time.sleep(2)

# Function to switch screens left
def switch_screen_left():
    pyautogui.hotkey('ctrl', 'left')
    time.sleep(2)

start_time = time.time()  # get the program start time
running = True

# Loop to run functions
while running:
    move_mouse()
    switch_screen_right()
    time.sleep(2)
    switch_screen_left()
    if KeyboardInterrupt: # User interrupt Ctrl+C
        pass
    elapsed_time = time.time() - start_time  
    if elapsed_time >= 3600:  # Abort after 60 minutes
        running = False  

exit()  