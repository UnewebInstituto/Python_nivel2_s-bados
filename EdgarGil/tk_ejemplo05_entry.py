import tkinter as tk

def imprimir_valor():
    print("contenido del valor ingresado", entrada.get())
    entrada.delete(0, tk.END)



ventana = tk.Tk()

entrada = tk.Entry(ventana, width=40)
boton = tk.Button(ventana, text ="obtener valor", command= imprimir_valor)
entrada.pack()
boton.pack()
ventana.mainloop()
