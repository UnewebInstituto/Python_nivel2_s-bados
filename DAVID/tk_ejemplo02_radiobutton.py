# Se le da un alias a la librería tkinter
import tkinter as tk 

def imprimir_seleccion():
    print("Opción seleccionada:", var.get())

# Se crea el objeto ventana a partir de la clase tkinter
ventana = tk.Tk()

var = tk.StringVar(value = "Opcion 1")

botonRadio1 = tk.Radiobutton(ventana,text="Estudia", varible=var, value="ESTUDIA", command=imprimir_seleccion)
botonRadio2 = tk.Radiobutton(ventana,text="Trabaja", varible=var, value="TRABAJA", command=imprimir_seleccion)
botonRadio3 = tk.Radiobutton(ventana,text="Otra", varible=var, value="OTRA", command=imprimir_seleccion)

botonRadio1.pack()
botonRadio2.pack()
botonRadio3.pack()

ventana.mainloop()

