#Estrella
import tkinter

root=Tk ()
canvas_width = 600
canvas_height = 600

root.geometry(f"{canvas_width}x{canvas_height}")
can_wigdt=Canvas(root,width=canvas_width,height=canvas_height)
can_widgt.pack()

points=[100,10,40,198,190,78,10,78,160,198]

can_widgt.create_polygon(points,outline='blue',fill='green',width=4)

root.mainloop()