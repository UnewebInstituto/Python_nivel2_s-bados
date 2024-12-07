import tkinter as tk

def imprimir_seleccion():
    print("prueba", var.get())
    
ventana = tk.Tk()
var  = tk.StringVar(value ="opcion 1")

checkButton1 = tk.Checkbutton(ventana, text = "estudia", variable = var, onvalue = "estudia",offvalue= "off", command=imprimir_seleccion)
checkButton2 = tk.Checkbutton(ventana, text = "trabaja", variable = var, onvalue = "trabaja",offvalue= "off", command=imprimir_seleccion)
checkButton3 = tk.Checkbutton(ventana, text = "otra", variable = var, onvalue = "otra",offvalue= "off", command=imprimir_seleccion)

checkButton1.pack()
checkButton2.pack()
checkButton3.pack()

ventana.mainloop()
