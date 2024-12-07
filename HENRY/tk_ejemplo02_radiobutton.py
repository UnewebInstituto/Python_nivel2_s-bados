# Se le da un alias a la librería tkinter
import tkinter as tk 
def imprimir_seleccion():
    print("Opción seleccionada:", var.get())
# Se crea el objeto ventana a partir de la clase tkinter
ventana = tk.Tk()
#Definición de variable a través de la cual se obtiene el valor seleccionado
#del radio button
var = tk.StringVar(value = "")
botonRadio1 = tk.Radiobutton(ventana,text="Estudia", variable=var, value="ESTUDIA", command=imprimir_seleccion)
botonRadio2 = tk.Radiobutton(ventana,text="Trabaja", variable=var, value="TRABAJA", command=imprimir_seleccion)
botonRadio3 = tk.Radiobutton(ventana,text="Otra", variable=var, value="OTRA", command=imprimir_seleccion)
botonRadio1.pack()
botonRadio2.pack()
botonRadio3.pack()
ventana.mainloop()
