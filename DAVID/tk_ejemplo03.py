# Se le da un alias a la librería tkinter
import tkinter as tk 
def imprimir_seleccion():
    print("Opción seleccionada:", var.get())
# Se crea el objeto ventana a partir de la clase tkinter
ventana = tk.Tk()

#Definición de variable a través de la cual se obtiene el valor seleccionado
#del radio button
var = tk.StringVar(value = "")

checkButton1 = tk.Checkbutton(ventana,text="Estudia", variable=var, onvalue="on", offvalue="off", command=imprimir_seleccion)

checkButton1.pack()

ventana.mainloop()
