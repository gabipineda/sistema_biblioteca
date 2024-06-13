import pickle
from typing import Dict, List

# Estructuras de datos para la biblioteca
libros = {}
usuarios = {}

# Funciones del sistema de gestión de biblioteca
def agregar_libro(titulo: str, autor: str) -> None:
    if titulo in libros:
        libros[titulo]['cantidad'] += 1
    else:
        libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}

def mostrar_libros() -> None:
    for titulo, detalles in libros.items():
        print(f"{titulo} por {detalles['autor']} - Cantidad: {detalles['cantidad']} - {'Disponible' if detalles['disponible'] else 'No Disponible'}")

def prestar_libro(titulo: str, nombre_usuario: str) -> None:
    if titulo in libros and libros[titulo]['disponible'] and nombre_usuario in usuarios:
        libros[titulo]['cantidad'] -= 1
        if libros[titulo]['cantidad'] == 0:
            libros[titulo]['disponible'] = False
        usuarios[nombre_usuario].append(titulo)

def registrar_usuario(nombre_usuario: str) -> None:
    usuarios[nombre_usuario] = []

def guardar_datos() -> None:
    with open('datos_biblioteca.pkl', 'wb') as archivo:
        pickle.dump((libros, usuarios), archivo)

def cargar_datos() -> None:
    try:
        with open('datos_biblioteca.pkl', 'rb') as archivo:
            global libros, usuarios
            libros, usuarios = pickle.load(archivo)
    except FileNotFoundError:
        pass

def listar_usuarios() -> None:
    for usuario in usuarios:
        print(usuario)

def listar_libros_de_usuarios(nombre_usuario: str) -> None:
    if nombre_usuario in usuarios:
        for titulo in usuarios[nombre_usuario]:
            print(titulo)

def devolver_libro(titulo: str, nombre_usuario: str) -> None:
    if titulo in usuarios[nombre_usuario]:
        usuarios[nombre_usuario].remove(titulo)
        libros[titulo]['cantidad'] += 1
        if libros[titulo]['cantidad'] > 0:
            libros[titulo]['disponible'] = True

# Ejemplo de uso
cargar_datos()
registrar_usuario('Juan Perez')
agregar_libro('El Principito', 'Antoine de Saint-Exupéry')
prestar_libro('El Principito', 'Juan Perez')
guardar_datos()




