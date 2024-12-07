# Se le da un alias a la librería tkinter
import tkinter as tk 

def imprimir_mensaje():
    print("Opcion seleccionada:", var.get())

#se crea el objeto ventana a partir de tk.Tk o la clase tkinnter
ventana = tk.Tk()
var = tk.StringVar(value= "Opcion 1")
botonrRadio1 = tk.Radiobutton(ventana, text ="Estudia", variable = var, value= "ESTUDIA", command= imprimir_mensaje)

botonrRadio2 = tk.Radiobutton(ventana, text ="Trabaja", variable = var, value= "TRABAJA", command= imprimir_mensaje)
botonrRadio3 = tk.Radiobutton(ventana, text ="otra", variable = var, value= "OTRA", command= imprimir_mensaje)

botonrRadio1.pack()
botonrRadio2.pack()
botonrRadio3.pack()


ventana.mainloop()
