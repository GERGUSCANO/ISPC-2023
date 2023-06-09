def ListarDatos(self):
    if self.conexion.is_connected():

    try:
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * from interprete"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
    