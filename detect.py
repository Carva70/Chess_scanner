from PIL.ImageOps import grayscale
from cv2 import polylines
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import sys

from stockfish import Stockfish
import webbrowser

#asdf 170 162 58

def blancas(x, y, t):
    if (pyautogui.locateOnScreen('piezas/peon_n.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'p'
    if (pyautogui.locateOnScreen('piezas/alfil_n.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'b'
    if (pyautogui.locateOnScreen('piezas/caballo_n.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'n'
    if (pyautogui.locateOnScreen('piezas/torre_n.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'r'
    if (pyautogui.locateOnScreen('piezas/dama_n.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'q'
    if (pyautogui.locateOnScreen('piezas/rey_n.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'k'
    return None

def negras(x, y, t):
    if (pyautogui.locateOnScreen('piezas/peon_b.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'P'
    if (pyautogui.locateOnScreen('piezas/alfil_b.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'B'
    if (pyautogui.locateOnScreen('piezas/caballo_b.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'N'
    if (pyautogui.locateOnScreen('piezas/torre_b.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'R'
    if (pyautogui.locateOnScreen('piezas/dama_b.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'Q'
    if (pyautogui.locateOnScreen('piezas/rey_b.png', region=(x,y,t,t), grayscale=True, confidence=0.8) != None):
        return 'K'
    return None

def impPieza(x, y, t):

    color1 = pyautogui.pixel(x + int(t / 2), y + int(t / 2))[0]
    color2 = pyautogui.pixel(x + int(t / 2), y + int(t / 2) - 10)[0]
    iml = pyautogui.screenshot(region=(x,y,t,t))
    iml.save(r"C:\Users\nacho\OneDrive\Escritorio\si\debug\im" + str(y) + "-" + str(int(x/100)) +  ".png")

    if  color1 == 0 or color2 == 0 :
        p = blancas(x, y, t)
        if p != None:
            return p
        else:
            return negras(x, y, t)

    elif color1 == 255 or color2 == 255:
        p = negras(x, y, t)
        if p != None:
            return p
        else:
            return blancas(x, y, t)

    return None
    

def main():
    stockfish = Stockfish(r"\Users\nacho\OneDrive\Escritorio\k\Stockfish12")
    tamano = 868
    posx = 514
    posy = 131
    div = int(tamano/8)
    string = ""
    color1 = pyautogui.pixel(517, 975)[0]
    if (pyautogui.locateOnScreen('piezas/h.png', region=(517, 975,20,20), grayscale=True, confidence=0.8) != None):
        reversed = True
    else:
        reversed = False
    next = 'w'
    
    print("FEN:")
    for y in range(0, tamano-div, div):
        count = 0
        for x in range(0, tamano-div, div):
            
            p = impPieza(x=posx+x, y=posy+y, t=div)
            if p != None:
                if (count != 0):
                    print(count, end='')
                    string += str(count)
                    sys.stdout.flush()
                    count = 0
                pixel = pyautogui.pixel(posx + x + 5, posy + y + 5)[0]
                if  pixel == 170 or pixel == 205:
                    if (p == 'P' or p == 'B' or p == 'R' or p == 'N' or p == 'Q' or p == 'K'):
                        next = 'b'
                print(p, end='')
                string += p
                sys.stdout.flush()
            else:
                count += 1
        if (count != 0):
            print(count, end='')
            string += str(count)
            sys.stdout.flush()
        if y < tamano-(div*2):
            print('/',end='')
            string += "/"
            sys.stdout.flush()
    
    if reversed == True:
        string = string[::-1]

    string += " " + next + " KQkq - 0 1"
    print()
    print(string)
    stockfish.set_fen_position(string)
    print(stockfish.get_board_visual())
    move = stockfish.get_best_move_time(5000)
    stockfish.make_moves_from_current_position([move])
    print(move)
    print(stockfish.get_board_visual())

    # string = stockfish.get_fen_position().replace(" ", "_") + "#0"
    # url = "https://lichess.org/analysis/standard/" + string
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # webbrowser.get(chrome_path).open(url)

    

if __name__ == "__main__":
    main()