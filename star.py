#Estrella
from tkinter import Canvas

c = Canvas() 
c.pack()
verts = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
for i in range(len(verts)): verts[i] += 100
c.create_polygon(verts, fill='blue', outline='red') 
c.mainloop()