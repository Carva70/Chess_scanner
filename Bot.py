from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X: 587 Y: 700 RGB: ( 0, 0, 0)
#Tile 2 Position: X: 682 Y: 700 RGB: ( 0, 0, 0)
#Tile 3 Position: X: 776 Y: 700 RGB: ( 0, 0, 0)
#Tile 4 Position: X: 871 Y: 700 RGB: ( 0, 0, 0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(587, 400)[0] == 0:
        click(587, 400)
    if pyautogui.pixel(682, 400)[0] == 0:
        click(682, 400)
    if pyautogui.pixel(776, 400)[0] == 0:
        click(776, 400)
    if pyautogui.pixel(871, 400)[0] == 0:
        click(871, 400)