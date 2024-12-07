import tkinter as tk 


def imprimir_mensaje():
    print("mensaje en consola: hola mundo")
    
ventana = tk.Tk()

boton = tk.Button(ventana, text = "mensaje", command = imprimir_mensaje)
boton.pack()

ventana.mainloop()