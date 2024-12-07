import tkinter as tk

def imprimir_valor():
    print("Contenido del valor ingresado:", entrada_1.get())
    print("Contenido del valor ingresado:", entrada_2.get())
    entrada_1.delete(0, tk.END)
    entrada_2.delete(0, tk.END)

ventana = tk.Tk()

entrada_1 = tk.Entry(ventana, width=40)
entrada_2 = tk.Entry(ventana, width=40)

boton = tk.Button(ventana, text="Obtener valor", command=imprimir_valor)

entrada_1.pack()
entrada_2.pack()

boton.pack()

ventana.mainloop()

