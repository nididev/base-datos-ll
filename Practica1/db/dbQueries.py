from utils.dbConnection import pool

def ReadPrestamosConUsuarioYLibro():
    """
    Obtiene todos los préstamos junto con el nombre del usuario y el nombre del libro asociado.
    """
    connection = pool()
    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)
        # Realizar un JOIN entre las tablas prestamos, usuarios y libros
        query = """
        SELECT 
            p.id_prestamo, 
            u.nombre AS nombre_usuario, 
            l.titulo AS nombre_libro,  -- Obtener el nombre del libro
            p.fecha_prestamo, 
            p.fecha_devolucion
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        JOIN libros l ON p.id_libro = l.id_libro  -- JOIN con la tabla libros
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"Error al obtener datos de préstamos: {e}")
        return []
    finally:
        if connection:
            connection.close()