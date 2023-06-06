import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        db= ''
    )
    if conexion.is_connected():
        print("la conexion fue exitosa")
except:
    print("No se pudo conectar la base de datos")

finally:
    if conexion.is_connected():
        conexion.close()
        print("la conexion fue cerrada")


def listardatos(self):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "SELECT * from interprete"
            cursor.execute(sentenciaSQL)
            resultados= cursor.fetchall()
            self.conexion.close()
            return resultados
        except mysql.connector.Error as descripcionError:
            print("¡No se conecto!", descripcionError)


def crearEntidad(self):
    if self.conexion.is_connected():
        try:
            cursor=self.conexion.cursor()
            sentenciaSQL="CREATE TABLE USUARIO (nombre varchar (30) not null, apellido varchar (30) not null, direccion varchar (50) not null, apellido int not null, fecha_nacimiento int not null)"
            cursor.execute(sentenciaSQL)
            self.conexion.close()
            return
        except mysql.connector.Error as descripcionError:
            print ("¡No se conecto!", descripcionError)

