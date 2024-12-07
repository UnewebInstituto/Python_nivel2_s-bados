
#alias a la libreria tkinter
import tkinter as tk

def imprimir_mensaje():
    print("MENSAJE EN CONSOLA: HOLA MUNDO")

venta= tk.Tk()
boton=tk.Button(venta,text="message", command= imprimir_mensaje)

boton.pack()
venta.mainloop()
