import mysql.connector

def pool():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",  
            user="nididev",  
            password=".Nidiandiego08",  
            database="biblioteca"  
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None