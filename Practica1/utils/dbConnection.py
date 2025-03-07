import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",  # Cambia si usas otro host
            user="nididev",  # Cambia por tu usuario de MySQL
            password=".Nidiandiego08",  # Cambia por tu contraseña
            database="biblioteca"  # Nombre de tu base de datos
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None