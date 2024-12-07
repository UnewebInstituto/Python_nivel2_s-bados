import tkinter as tk

ventana = tk.Tk()
colores =["red", "blue","green"]
canvas_1 = tk.Canvas(ventana, width=300, height=200)
canvas_1.pack()
for
rectangulo = canvas_1.create_rectangle(0, 0, 50, 50, fill="blue")

ventana.mainloop()