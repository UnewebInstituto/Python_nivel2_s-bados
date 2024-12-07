import mysql.connector
myDB = mysql.connector.connect(host="localhost",user="root",passwd="",database="bdpyn2_henry")
comando = myDB.cursor()