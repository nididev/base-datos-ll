from db.dbFunctions import ReadBooks, CreateBook, ReadUser, CreateUser, CreatePrestamo, RegistrarDevolucion
from db.dbQueries import ReadPrestamosConUsuarioYLibro 
from datetime import datetime
import os
from rich.console import Console
from rich.table import Table

# Configurar rich para diseño en consola
console = Console()

# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Ver todos los libros")
    print("2. Registrar un nuevo libro")
    print("3. Registrar un nuevo usuario")
    print("4. Ver todos los usuarios")
    print("5. Registrar un préstamo")
    print("6. ver todos los préstamos")
    print("7. Registrar una devolucion de un préstamo")
    print("8. Salir")

# Función para mostrar la lista de libros en una tabla
def mostrarLibros():
    libros = ReadBooks()  # Obtener todos los libros
    if libros:
        # Crear una tabla con rich
        table = Table(title="Lista de Libros", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Título", style="bold")
        table.add_column("Autor")
        table.add_column("Categoría")
        table.add_column("Disponible", justify="center")

        # Agregar cada libro a la tabla
        for libro in libros:
            disponible = "✅" if libro['disponible'] else "❌"
            table.add_row(
                str(libro['id_libro']),
                libro['titulo'],
                libro['autor'],
                libro['categoria'],
                disponible
            )
        console.print(table)  # Mostrar la tabla
    else:
        console.print("[bold red]No se encontraron libros.[/bold red]")

def mostrarPrestamos():
    prestamos = ReadPrestamosConUsuarioYLibro()  # Obtener préstamos con nombres de usuarios y libros
    if prestamos:
        # Crear una tabla con rich
        table = Table(title="Lista de Préstamos", show_header=True, header_style="bold green")
        table.add_column("ID Préstamo", style="dim", width=10)
        table.add_column("Nombre Usuario", style="bold", width=20)
        table.add_column("Nombre Libro", style="bold", width=30)  # Mostrar el nombre del libro
        table.add_column("Fecha Préstamo", justify="center")
        table.add_column("Fecha Devolución", justify="center")

        # Agregar cada préstamo a la tabla
        for prestamo in prestamos:
            # Convertir las fechas a cadenas
            fecha_prestamo = str(prestamo['fecha_prestamo'])
            fecha_devolucion = str(prestamo['fecha_devolucion'])

            table.add_row(
                str(prestamo['id_prestamo']),
                prestamo['nombre_usuario'],  # Mostrar el nombre del usuario
                prestamo['nombre_libro'],   # Mostrar el nombre del libro
                fecha_prestamo,             # Usar la fecha convertida a cadena
                fecha_devolucion            # Usar la fecha convertida a cadena
            )
        console.print(table)  # Mostrar la tabla
    else:
        console.print("[bold red]No se encontraron préstamos.[/bold red]")

def mostrarUsuarios():
    usuarios = ReadUser()  # Obtener todos los usuarios
    if usuarios:
        # Crear una tabla con rich
        table = Table(title="Lista de Usuarios", show_header=True, header_style="bold cyan")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Nombre", style="bold")
        table.add_column("Correo")

        # Agregar cada usuario a la tabla
        for usuario in usuarios:
            table.add_row(
                str(usuario['id_usuario']),
                usuario['nombre'],
                usuario['correo']
            )
        console.print(table)  # Mostrar la tabla
    else:
        console.print("[bold red]No se encontraron usuarios.[/bold red]")

def main():
    while True:
        limpiar_consola()  # Limpiar la consola
        mostrar_menu()  # Mostrar el menú
        opcion = input("Seleccione una opción: ")  # Leer la opción del usuario

        if opcion == "1":
            limpiar_consola()
            mostrarLibros()  # Mostrar la lista de libros
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            limpiar_consola()
            print("\n--- Registrar Nuevo Libro ---")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            disponible = input("¿Está disponible? (1 para Sí, 0 para No): ")

            if disponible not in ["0", "1"]:
                print("Error: Disponible debe ser 0 (No) o 1 (Sí).")
                input("\nPresione Enter para continuar...")
                continue

            if CreateBook(titulo, autor, categoria, int(disponible)):
                print("Libro registrado exitosamente.")
            else:
                print("Error al registrar el libro.")

            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            limpiar_consola()
            print("\n--- Crear Nuevo Usuario ---")
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo electrónico del usuario: ")

            if CreateUser(nombre, correo):
                print("Usuario creado exitosamente.")
            else:
                print("Error al crear el usuario.")

            input("\nPresione Enter para continuar...")

        if opcion == "4":
            limpiar_consola()
            mostrarUsuarios()  # Mostrar la lista de libros
            input("\nPresione Enter para continuar...")

        elif opcion == "5":
            limpiar_consola()
            print("\n--- Registrar Préstamo ---")
            mostrarLibros()  # Mostrar la lista de libros
            id_libro = input("\nIngrese el ID del libro: ")

            mostrarUsuarios()  # Mostrar la lista de usuarios
            id_usuario = input("\nIngrese el ID del usuario: ")

            # Solicitar fechas de préstamo y devolución
            fecha_prestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
            fecha_devolucion = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")

            # Validar que las fechas tengan el formato correcto
            try:
                datetime.strptime(fecha_prestamo, "%Y-%m-%d")
                datetime.strptime(fecha_devolucion, "%Y-%m-%d")
            except ValueError:
                print("Error: Formato de fecha incorrecto. Use YYYY-MM-DD.")
                input("\nPresione Enter para continuar...")
                continue

            # Registrar el préstamo
            if CreatePrestamo(int(id_usuario), int(id_libro), fecha_prestamo, fecha_devolucion):
                print("Préstamo registrado exitosamente.")
            else:
                print("Error al registrar el préstamo.")

            input("\nPresione Enter para continuar...")

        elif opcion == "6":
            limpiar_consola()
            mostrarPrestamos()  # Mostrar la lista de préstamos
            input("\nPresione Enter para continuar...")
        
        elif opcion == "7":
            limpiar_consola()
            print("\n--- Registrar Devolución ---")
            mostrarPrestamos()  # Mostrar la lista de préstamos
            id_prestamo = input("\nIngrese el ID del préstamo a devolver: ")

            # Registrar la devolución
            if RegistrarDevolucion(int(id_prestamo)):
                print("Devolución registrada exitosamente.")
            else:
                print("Error al registrar la devolución.")

            input("\nPresione Enter para continuar...")

        elif opcion == "8":
            print("Saliendo del sistema...")
            break  # Salir del bucle y terminar el programa

        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
    