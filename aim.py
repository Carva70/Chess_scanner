from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# 255, 219, 195

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(658,336,610,430))
    ancho, alto = pic.size
    salto = 5
    count = 0

    for x in range(0, ancho, salto):
        for y in range(0, alto, salto):
            r, g, b = pic.getpixel((x, y))
            if (b == 195):
                click(x + 658, y + 336)
                ++count
                time.sleep(0.05)
                break

    print(count)
