#Bits Of Fun
import tkinter

screen = tkinter.Tk()
screen.geometry("400x300")

def entry1():
    print ("El primer videojuego es 'Post - D Day'. Fue lanzado el 4 de junio de 2020 en Itch.io, completamente gratis.")

def entry2():
    print ("El segundo videojuego es 'Poligon: Fall Of The Light' Actualmente está en fase de desarrollo, se estima que saldrá a fines de septiembre o comienzos de octubre.")

def entry3():
    print ("El tercer videojuego es 'The StoryTeller'. Actualmente está siendo documentado, y se estima que su desarrollo comenzará en las vacaciones de invierno y primavera de este año.")

def entry4():
    print ("El cuarto videojuego es 'Lights Off'. Por ahora esta su version en texto escrita en Python hace una semana, pero será documentada durante estas semanas para su futuro lanzamiento a fines de este año.")

label = tkinter.Label(screen, text = "Bits Of Fun", bg = "red", font = "Arial 15")
b1 = tkinter.Button(screen, text = "Juego 1",  bg = "orange", width = 5, height = 5, command = entry1)
b2 = tkinter.Button(screen, text = "Juego 2", bg = "green", width = 5, height = 5, command = entry2)
b3 = tkinter.Button(screen, text = "Juego 3",  bg = "blue", width = 5, height = 5, command = entry3)
b4 = tkinter.Button(screen, text = "Juego 4", bg = "yellow", width = 5, height = 5, command = entry4)

label.grid(row = 0, column = 0, padx = 5, pady = 5)
b1.grid(row = 1, column = 0, padx = 5, pady = 5)
b2.grid(row = 2, column = 0, padx = 5, pady = 5)
b3.grid(row = 3, column = 0, padx = 5, pady = 5)
b4.grid(row = 4, column = 0, padx = 5, pady = 5)

screen.mainloop()
