# Robotic Mouse and Keyboard 🤖
This is a Python script that uses the pyautogui library to automate the movement of the mouse cursor and switching between screens. The script is designed to run for a maximum of one hour and can be interrupted by pressing Ctrl + C.

# Prerequisites 💻
Before running the script, you will need to install the pyautogui library.

```python
pip install pyautogui
```
# How to Run the Script 🛠

- Download and save the python file **main.py** to your local machine.

- Run the script in your chosen code editor

- The script will start running and the mouse cursor will move 10 units to the right and then to the left repeatedly. It will also switch between screens using the ctrl + right and ctrl + left hotkeys.

- The script will run for a maximum of one hour, after which it will automatically exit.

- You can interrupt the script at any time by pressing Ctrl + C.

# Notes 🔑
The pyautogui.FAILSAFE variable is set to True, which means that the script will abort if you move the mouse cursor to the upper-left corner of the screen. This is a safety feature to prevent the script from running indefinitely if something goes wrong.

The time.sleep() function is used to introduce a delay between each action. This is to ensure that the script does not run too fast and confuse the computer.

The KeyboardInterrupt exception is used to catch the Ctrl + C interrupt and allow the script to exit gracefully.

This script introduces the idea of using robotic processes to automate computer control for ethical and non-harmful use cases only.