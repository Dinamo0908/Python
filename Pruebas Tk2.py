#Testeo 2
import tkinter

screen = tkinter.Tk()
screen.geometry("800x600")

b1 = tkinter.Label(screen, text = "b1", width = 10, height = 5)
b2 = tkinter.Label(screen, text = "b2",  width = 10, height = 5)
b3 = tkinter.Label(screen, text = "b3",  width = 10, height = 5)

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)

screen.mainloop()
