import Conexion_mysql
import sys
miRuta_Pgm = "C:\PYTHON_NIVEL2_SAB_20241123\MartinDLR"
try:
    sys.path.index(miRuta_Pgm )
except:
    sys.path.append(miRuta_Pgm)
continuar =''
while True:
    sql = "INSERT INTO personas (cedula, nombre, apellido, direccion , fechnac) VALUES(%s,%s,%s,%s,%s)"
    print("Ingrese los datos solicitados...")
    cedulaTmp = input("cedula:")
    nombreTMP = input("nombre:")
    apellidoTmp = input("apellido:")
    direccionTmp = input("direccion:")
    fechnacTmp = input("Fecha nacimiento fomato AAAA-MM-DD:")
    valores = (cedulaTmp, nombreTMP, apellidoTmp, direccionTmp , fechnacTmp)
    #try:
    Conexion_mysql.comando(sql, valores)
    Conexion_mysql.mibase_de_datos.commit()
    #except:
    #    print("no se pudo realizar la operacion sobre la tabla")
    continuar = input("Desea ingresar otra persona s/n: ") 
    if (continuar.upper() =='S'):
        continue
    else:
        break
Conexion_mysql.mibase_de_datos.close()
