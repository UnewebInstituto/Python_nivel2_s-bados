import conexion
import sys
miRuta_Pgm = "C:\PYTHON_NIVEL2_SAB_20241123\MartinDLR"
try:
    sys.path.index(miRuta_Pgm )
except:
    sys.path.append(miRuta_Pgm)
continuar =''
while True:
    sql = "select * from personas"
    sql2 = "describe personas"
    #try:
    conexion.comando(sql)
    print("contenido de la tabla PERSONAS".center(60,"-"))
    print("id cedula nombre apellido direccio fecha_nac")
    for datos in conexion.comando.fetchall():
        print(datos[0],  datos[1],datos[2],datos[3],datos[4],datos[5])
          
    continuar = input("Desea ingresar otra persona s/n: ") 
    if (continuar.upper() =='S'):
        continue
    else:
        break
conexion.mibase_de_datos.close()
