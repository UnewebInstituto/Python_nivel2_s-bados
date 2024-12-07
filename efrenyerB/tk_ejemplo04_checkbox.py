# Se le da un alias a la librería tkinter
import tkinter as tk 

def imprimir_seleccion():
    seleccionados = [opcion for opcion, estado in opciones.items() if estado.get()]
    print("Opciones seleccionadas:", seleccionados)

# Se crea el objeto ventana a partir de la clase tkinter
ventana = tk.Tk()

# Definición de un diccionario para almacenar el estado de cada Checkbutton
opciones = {
    "ESTUDIA": tk.BooleanVar(),
    "TRABAJA": tk.BooleanVar(),
    "OTRA": tk.BooleanVar()
}

# Creación de los Checkbuttons
checkButton1 = tk.Checkbutton(ventana, text="Estudia", variable=opciones["ESTUDIA"], command=imprimir_seleccion)
checkButton2 = tk.Checkbutton(ventana, text="Trabaja", variable=opciones["TRABAJA"], command=imprimir_seleccion)
checkButton3 = tk.Checkbutton(ventana, text="Otra", variable=opciones["OTRA"], command=imprimir_seleccion)

# Empaquetar los Checkbuttons en la ventana
checkButton1.pack()
checkButton2.pack()
checkButton3.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()