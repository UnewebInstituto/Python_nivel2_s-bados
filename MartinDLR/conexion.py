import mysql.connector
mibase_de_datos = mysql.connector.connect(host = "localhost",   user = "root", passwd = "", database = "bdpyn2_martindlr")
comando = mibase_de_datos.cursor()