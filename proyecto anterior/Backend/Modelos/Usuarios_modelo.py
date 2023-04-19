import mysql.connector

class Usuarios():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = '192.168.0.13',
                port = 3306,
                user = 'Pablo',
                password = '12345',
                db = 'arsalud'
            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)

#CREATE O INSERT.
    def InsertarValor(self, nombre, apellido, correo, direccion, telefono, id_rol):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO usuarios (nombre, apellido, correo, direccion, telefono, id_rol) VALUES(%s,%s,%s,%s,%s,%s)"
                data= (nombre, apellido, correo, direccion, telefono, id_rol)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")
                print(sentenciaSQL, data)
#READ O LEER
    def BuscarObjeto(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "SELECT * from usuarios"
           
                cursor.execute(sentenciaSQL)
                resultadoREAD = cursor.fetchall()
                self.conexion.close()
                return resultadoREAD

            except:
                print("No se pudo concectar a la base de datos")

#UPDATE O ACTUALIZAR.
    def ActualizarValor(self, ID, Nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "UPDATE usuarios SET nombre = '"+ Nombre + "' where id = " + str(ID)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")
                print(sentenciaSQL)

#DELETE O ELIMINAR
    def EliminarObjeto(self,ID):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM usuarios where id = " + str(ID)
                
                cursor.execute(sentenciaSQL)

                self.conexion.commit()                
                self.conexion.close()
            except:
                print("No se pudo concectar a la base de datos")
                


pruebas = Usuarios()


# pruebas.EliminarObjeto(8)

# pruebas.ActualizarValor(1, "Sofia")

# pruebas.InsertarValor("Taty", "Oyola", "taty@gmail.com", "Belgrano 60", "035115604053", 1)

valores = pruebas.BuscarObjeto()

for valor in valores:
    print(valor[1])