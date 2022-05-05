from tkinter import N
import pyautogui as pt 
from time import sleep 
import pyperclip 
import random 

sleep(5)

posicao1 = pt.locateOnScreen("whatsapp/smyle.png", confidence=.6)
x = posicao1[0]
y = posicao1[1]

def receber_mensagem():
    global x, y 

    posicao = pt.locateOnScreen("whatsapp/smyle.png", confidence=.6)
    x = posicao[0]
    y = posicao[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x + 60, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_mensagem = pyperclip.paste()
    pt.click()
    print("mensagem recebida: " + whatsapp_mensagem)

    return whatsapp_mensagem

def resposta_post(mensagem): 
    global x, y 


    posicao = pt.locateOnScreen("whatsapp/smyle.png", confidence=.6)
    x = posicao[0]
    y = posicao[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(mensagem, interval=.01)
    pt.typewrite("\n", interval=.2)


def processo_resposta(mensagem):
    nao_aleatorio = random.randrange(3)

    if "?" in str(mensagem).lower():
        return "estou sendo habilitada pela minha genia 'jessica', se acalme, logo conseguirei responder perguntas."

    else:
        if nao_aleatorio == 0:
            return "isso e legal, mas e quando vai paga minha pizza!"
        elif nao_aleatorio == 1:
            return "nao se esqueca de me pagar um x salada"           
        else:
            return "ate mais!, ta me devendo um dogao"   

def verificar_novas_mensagens():
    pt.moveTo(x + 50, y - 40, duration=.5)

    while True:
        try:
            posicao = pt.locateOnScreen("whatsapp/ponto_verde.png", confidence=.7)

            if posicao is not None:
                pt.moveTo(posicao)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.6)

        except(Exception):
            print("não há novas mensagens")            

        if pt.pixelMatchesColor(int(x + 50), int(y - 40), (255,255,255), tolerance=10):
            print("e_branco")
            processo_mensagem = processo_resposta(receber_mensagem())
            resposta_post(processo_mensagem)
        else:
            print("não há novas mensagens")
        sleep(6)        
                       
      

verificar_novas_mensagens()