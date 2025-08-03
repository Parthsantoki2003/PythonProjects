import pyautogui as pag
import random
import time

while True:
    x=random.randint(500,800)
    y=random.randint(200,500)
    pag.moveTo(x,y,0.5)
    time.sleep(2)