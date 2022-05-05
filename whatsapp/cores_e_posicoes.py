import pyautogui as pt 
from time import sleep 

while True:
    posicaoXY = pt.position()
    print(posicaoXY, pt.pixel(posicaoXY[0], posicaoXY[1]))
    sleep(1)
    if posicaoXY[0] == 0:
        break
    