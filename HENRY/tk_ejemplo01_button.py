# Se le da un alias a la librería tkinter
import tkinter as tk 

def imprimir_mensaje():
    print("Mensaje en consola: Hola Mundo")

ventana = tk.Tk()

boton = tk.Button(ventana, text="Emitir mensaje", command=imprimir_mensaje)
boton.pack()

ventana.mainloop()
