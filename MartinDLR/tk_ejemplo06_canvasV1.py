import tkinter as tk

ventana = tk.Tk()

canvas_1 = tk.Canvas(ventana, width=300, height=200)
canvas_1.pack()

rectangulo = canvas_1.create_rectangle(0, 0, 50, 50, fill="blue")

ventana.mainloop()