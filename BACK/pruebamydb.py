import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '1996',
        db='AR_salud'
    )
    if conexion.is_connected():
        print("LA CONEXION FUE EXITOSA")
except:
    print("NO SE PUDO CONECTAR A LA BASE DE DATOS")


finally:
    if conexion.is_connected():
        conexion.close()
    print("LA CONEXION FUE CERRADA")
