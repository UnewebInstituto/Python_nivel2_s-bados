# Se le da un alias a la librería tkinter
import tkinter as tk 
def imprimir_seleccion():
    print("Opción seleccionada:", var.get())
# Se crea el objeto ventana a partir de la clase tkinter
ventana = tk.Tk()

#Definición de variable a través de la cual se obtiene el valor seleccionado
#del radio button
var = tk.StringVar(value = "")

checkButton1 = tk.Checkbutton(ventana,text="Estudia", variable=var, onvalue="estudia", offvalue="off", command=imprimir_seleccion)

checkButton2 = tk.Checkbutton(ventana,text="trabaja", variable=var, onvalue="trabaja", offvalue="off", command=imprimir_seleccion)

checkButton3 = tk.Checkbutton(ventana,text="otra", variable=var, onvalue="otra", offvalue="off", command=imprimir_seleccion)
checkButton1.pack()
checkButton2.pack()
checkButton3.pack()

ventana.mainloop()

