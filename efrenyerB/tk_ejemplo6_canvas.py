import tkinter as tk

ventana=tk.Tk()

#crea el canvas

canvas_1=tk.Canvas(ventana,width=300, height=200)
colores=["red","green", "blue"]
x=0
y=0
lado=50


for i in range(3):
    rectangulo= canvas_1.create_rectangle(x,y, x+lado, y+lado, fill=colores[i])
    
    x += lado 
    y += lado


canvas_1.pack()

ventana.mainloop()

