#importujemy z tkintera:
from fileinput import filename
import tkinter as tk
from tkinter import Label, filedialog , Text
import os

#"głowa" naszego programu:
root = tk.Tk ()
root.title ('Bursztynek')
apps = []

#Część odpowiedzialna za przywoływanie zapisanej aplikacji po ponownym otwarciu (komentarz ,,X''):
if os.path.isfile ('save.txt'):
   with open ('save.txt', 'r') as f:
       tempApps = f.read ()
       tempApps = tempApps.split (',')
       apps = [x for x in tempApps if x.strip()]

#tworzymy funkcję addApp odpowiedzialną za dodawanie aplikacji, do której "podłączony" jest przycisk w aplikacji:
def addApp ():
    for widget in frame.winfo_children(): 
        widget.destroy ()

    filename = filedialog.askopenfilename(initialdir='/', title = 'select file', filetypes = (("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg = 'gray')
        label.pack()

#tworzymy funkcję runApps odpowiedzialną za otwieranie aplikacji, do której "podłączony" jest przycisk w aplikacji:
def runApps():
    for app in apps:
        os.startfile(app)

#tutaj określamy wgląd interfesju:
canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42")
canvas.pack ()
frame = tk.Frame (root, bg = "#000000")

frame.place (relwidth = 0.8 , relheight = 0.8 , relx = 0.1 , rely = 0.1 )

#tutaj określamy jak wyglądają przyciski odpowiedzielne za dodawanie i otwieranie aplikacji, funkcją "command" podłączam je pod funkcje odpowiedzialne za otwieranie i dodawanie aplikacji (ich kod znajduje się powyżej)
openFile = tk.Button (root, text = " Open File ", padx = 10, pady = 5, fg = "#000000", bg = "#263D42", command = addApp)
openFile.pack ()

runApps = tk.Button (root, text = " Run Apps ", padx = 10, pady = 5, fg = "#000000", bg = "#263D42", command = runApps)
runApps.pack ()

#loading saved apps (komentarz ,,X''):
for app in apps:
    label = tk.Label (frame, text = app)
    label.pack()

#odpalenie aplikacji:
root.mainloop ()

#część odpowiedzialna za zapisanie wybranych aplikacji, aby po zamknięciu nie trzeba byłoby ich wybierać ponownie (komentarz ,,X''):
with open ('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')