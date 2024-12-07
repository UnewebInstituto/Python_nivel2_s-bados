import tkinter as tk

def imprimir_seleccion():
    print("prueba")
    
ventana = tk.Tk()
var  = tk.StringVar(value ="opcion 1")

botonRadio1 = tk.Radiobutton(ventana, text = "estudia", variable = var, value = "ESTUDIA", command=imprimir_seleccion)
botonRadio2 = tk.Radiobutton(ventana, text= "trabaja", variable = var, value= "TRABAJA", command=imprimir_seleccion)
botonRadio3 = tk.Radiobutton(ventana, text= "otra", variable = var, value= "OTRA", command=imprimir_seleccion)

botonRadio1.pack()
botonRadio2.pack()
botonRadio3.pack()

ventana.mainloop()
