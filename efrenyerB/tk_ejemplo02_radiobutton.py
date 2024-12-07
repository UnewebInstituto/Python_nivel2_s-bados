
#alias a la libreria tkinter
import tkinter as tk

def imprimir_mensaje():
    print("Opcion seleccionada: ",var.get())

venta= tk.Tk()
var=tk.StringVar(value= "Opcion 1")
botonRadio=tk.Radiobutton(venta,text="ESTUDIA",variable=var, value="ESTUDIA", command=imprimir_mensaje)

botonRadio2=tk.Radiobutton(venta,text="TRABAJA",variable=var, value="TRABAJA", command=imprimir_mensaje)

botonRadio3=tk.Radiobutton(venta,text="OTRO",variable=var, value="OTRO", command=imprimir_mensaje)

botonRadio.pack()
botonRadio2.pack()
botonRadio3.pack()
venta.mainloop()
