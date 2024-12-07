import sys
miRuta = ('c:/PYTHON_NIVEL2_SAB_20241123/EdgarGil')
try:
    sys.path.index(miRuta)
except:
    sys.path.append(miRuta)
import conexion
while True:
    print("Por favor ingrese los siguientes datos.")
    cedulaTmp = input("Cédula:")
    nombreTmp = input("Nombre:")
    apellidoTmp = input("Apellido:")
    direccionTmp = input("Dirección:")
    fechanacTmp = input("Fecha nacimiento (AAAA-MM-DD):")

    sql = "INSERT INTO personas(cedula, nombre, apellido, direccion, fechanac) VALUES (%s, %s, %s, %s, %s)"

    valores = (cedulaTmp, nombreTmp, apellidoTmp, direccionTmp, fechanacTmp)

    try:
        conexion.comando.execute(sql, valores)
        conexion.myDB.commit()
    except:
        print("Error: Falló el ingreso de los datos en Personas")

    continuar = input("¿Desea ingresar los datos de otra persona (S/N)?")
    if continuar.upper() == "S":
        continue
    else:
        break