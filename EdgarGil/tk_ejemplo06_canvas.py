import tkinter as tk

ventana= tk.Tk()

colores = ["red", "green", "blue"]

canvas_1 = tk.Canvas(ventana, width=300, height=200)
canvas_1.pack()

rectangulo = canvas_1.create_rectangle(0, 0, 50, 50, fill=colores[0])
rectangulo = canvas_1.create_rectangle(50, 50, 100, 100, fill=colores[1])
rectangulo = canvas_1.create_rectangle(100, 100, 150, 150, fill=colores[2])

       


ventana.mainloop()

