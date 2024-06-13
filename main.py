# main.py
import sys
from datos_biblioteca1 import (agregar_libro, mostrar_libros, prestar_libro, # type: ignore
                                registrar_usuario, guardar_datos, cargar_datos,
                                listar_usuarios, listar_libros_de_usuarios,
                                devolver_libro)

def menu_principal():
    while True:
        print("""
        Sistema de Gestión de Biblioteca
        1. Agregar Libro
        2. Mostrar Libros
        3. Prestar Libro
        4. Registrar Usuario
        5. Guardar Datos
        6. Cargar Datos
        7. Listar Usuarios
        8. Listar Libros de Usuarios
        9. Devolver Libro
        0. Salir
        """)
        opcion = input("Ingrese la opción deseada: ")
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            agregar_libro(titulo, autor)
        elif opcion == '2':
            mostrar_libros()
        elif opcion == '3':
            titulo = input("Ingrese el título del libro a prestar: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            prestar_libro(titulo, nombre_usuario)
        elif opcion == '4':
            nombre_usuario = input("Ingrese el nombre del nuevo usuario: ")
            registrar_usuario(nombre_usuario)
        elif opcion == '5':
            guardar_datos()
        elif opcion == '6':
            cargar_datos()
        elif opcion == '7':
            listar_usuarios()
        elif opcion == '8':
            nombre_usuario = input("Ingrese el nombre del usuario para listar sus libros: ")
            listar_libros_de_usuarios(nombre_usuario)
        elif opcion == '9':
            titulo = input("Ingrese el título del libro a devolver: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            devolver_libro(titulo, nombre_usuario)
        elif opcion == '0':
            guardar_datos()
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    cargar_datos()  # Carga los datos al iniciar el programa
    menu_principal()
