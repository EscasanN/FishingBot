from pyautogui import *
import pyautogui
import time 
import keyboard
import win32api, win32con

# functions for the mouse
def r_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


print("""****************************************
     Minecraft autofishing script
****************************************
Author: @EscasanN

------------HOW TO USE------------
1. Play Minecraft Java.
2. Set the language to English (American).
3. Turn subtitles ON.
4. Put a fishing rod in your hand and look at water.
5. AFK.

You can turn off the script by pressing the "q" key on the keyboard.
""")

print("The script will automatically start when you press enter.\nYou'll have 5 seconds to change the screen to Minecraft after that.")
input("Press 'Enter' to start>>>")

time.sleep(5)  # for alt-tabbing

# main loop
while keyboard.is_pressed('q') == False:

    # check if we are currently NOT fishing
    if pyautogui.locateOnScreen('Resources/splashing.png', grayscale=True, confidence=0.8) == None:
        # start fishing
        r_click()
        time.sleep(2)


    # check for a bite
    if pyautogui.locateOnScreen('Resources/fish_splash.png', grayscale=True, confidence=0.8) != None:
        # a fish bit!
        r_click()
        time.sleep(3)
