import pyautogui as pg
import time
import random

bad_words = ['puka', 'howle', 'moddaga', 'pichi gudha', 'modda gudu']
welcome = ['hello', 'hi', 'hey',]
love = ['I Love You']

time.sleep(8)

for i in range(1):
    a = random.choice(love)
    pg.write(a)
    pg.press('enter')
