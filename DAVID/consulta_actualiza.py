import sys
miRuta = 'c:/PYTHON_NIVEL2_SAB_20241123/DAVID'
try:
    sys.path.index(miRuta)
except:
    sys.path.append(miRuta)
import conexion
while True:
    sql = "SELECT * FROM personas"
    conexion.comando.execute(sql)
    print("Contenido de la tabla Personas".center(60,"-"))
    print("id Cédula Nombre Apellido Dirección Fecha nacimiento")
    for datos in conexion.comando.fetchall():
        print(datos[0], datos[1], datos[2], datos[3], datos[4],datos[5])
    while True:
        try:
            id = int(input("Ingrese el id del registro a modificar la dirección:"))
            break
        except ValueError:
            print("Debe ingresar un valor númerico entero.")
            continue
    sql = "SELECT * FROM personas WHERE id = %s"
    idBuscar = (id,)
    conexion.comando.execute(sql, idBuscar)
    datos = conexion.comando.fetchall()
    print("Detalle del registro consultado".center(60,"-"))
    print("Id:", datos[0])
    print("Cédula:", datos[1])
    print("Nombre:", datos[2])
    print("Apellido:", datos[3])
    print("Fecha Nacimiento:", datos[5])
    print("Dirección Actual:", datos[4])
    nuevaDireccion = input("Nueva dirección:")
    if (nuevaDireccion.isspace):
        nuevaDireccion = datos[4]
    sql = "UPDATE personas SET direccion = %s WHERE id = %s"
    valores = (nuevaDireccion, idBuscar)
    conexion.comando.execute(sql, valores)
    conexion.myDB.commit()
    if (conexion.comando.rowcount > 0):
        print("Registro fue actualizacdo con éxito")
    else:
        print("Atención: Registro no actualizado")
    continuar = input("¿Desea continuar (S/N)?")
    if continuar.upper() == "S":
        continue
    else:
        conexion.myDB.close()
        break
