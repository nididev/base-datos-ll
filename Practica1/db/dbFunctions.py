from utils.dbConnection import get_connection

def get_data_from_table():
    connection = get_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)  # Devuelve los datos como diccionario
        cursor.execute("SELECT * FROM libros")  # Reemplaza con tu tabla
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return []
    finally:
        if connection:
            connection.close()