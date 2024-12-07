# Se le da un alias a la librería tkinter
import tkinter as tk 

def imprimir_mensaje():
    print("Opcion seleccionada:", var.get())

#se crea el objeto ventana a partir de tk.Tk o la clase tkinnter
ventana = tk.Tk()
var = tk.StringVar(value= " ")
CheckButton1 = tk.Checkbutton(ventana, text ="Estudia", variable = var, onvalue= "on", offvalue="off", command= imprimir_mensaje)


CheckButton1.pack()
"""
botonrRadio2.pack()
botonrRadio3.pack()
"""

ventana.mainloop()
