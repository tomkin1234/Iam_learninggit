#importowanie modułu
from pdb import Restart
from random import random
import random
from tkinter import *

#tworzenie GUI
t = Tk()
t.title("Loteria")
t.geometry("300x350")

#tworzenie losy do loterii
#tworzymy przyciski z komendą global aby można było swobodnie i bez większych problemów zmieniać ilość przycisków
def wstaw_przyciski ():
    ile_przycisków = 1
    global przyciski
    przyciski = []
    #tworzymy przyciski oraz jeden prawidłowy, losowy los(przycisk, po którym wygrywamy grę)
    dobry = random.randint(0, ile_przycisków - 1)
    for i in range (ile_przycisków):
        if i == dobry:
         przyciski.append(Button(t, text = "Wylosuj mnie!", command = trafiony))
        else:
         przyciski.append(Button(t, text = "Wylosuj mnie!", command = pudło))
    #przyciski zajmują sutomatycznie całe okno
    for i in przyciski:
        i.pack(fill = BOTH, expand = YES)

def restart ():
     etykieta.destroy ()
     wstaw_przyciski ()
   
def pudło ():
    for i in przyciski:
        i.destroy ()
    global etykieta
    etykieta = Label(t, text = "PRZEGRAŁEŚ")
    etykieta.pack (fill = BOTH, expand = YES)
    t.after(2000, restart)

def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta 
    etykieta = Label(t, text = "WYGRAŁEŚ")
    etykieta.pack (fill = BOTH, expand = YES)
    #restert gry po 5000 milisekundach
    t.after (2000, restart)

wstaw_przyciski ()
mainloop ()




