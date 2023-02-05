#Testeo
import tkinter

screen = tkinter.Tk()
screen.geometry("800x600")

label = tkinter.Label(screen, text = "Bits Of Fun", bg = "red")
label.pack(fill = tkinter.X)

label2 = tkinter.Label(screen, pady = 40)
label2.pack()

def info():
    print("Datos del videojuego")

def macion(name):
    print ("Otros datos " + name)

def entry():
    inputE = textBox.get()
    label["text"] = inputE
    if inputE == "Que onda perri":
     print ("Tas re ido wachin")

textBox = tkinter.Entry(screen, font = "Arial 20")
textBox.pack()



b1 = tkinter.Button(screen, text = "Presiona", padx = 40, pady = 40, command = entry)
b2 = tkinter.Button(screen, text = "Aqui", padx = 40, pady = 40, command = lambda: macion("agustin"))
b1.pack()
b2.pack()

screen.mainloop()