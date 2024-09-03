import csv
import os

class Libro:
    """
    Definicion de la clase libro.

    Atributos:
        Titulo
        Autor
        Genero
        Puntuacion
    """
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} - Género: {self.genero} - Puntuación: {self.puntuacion}"

# Lista para almacenar los libros
lista_libros = []

def refresh_libros():
    # Creación de objetos de la clase Libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
    libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
    libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
    libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
    libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
    libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
    libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
    libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
    libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)

    lista_libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]

def cargar_libros_desde_csv(nombre_archivo):
    """
    Carga libros en lista_libros desde un CSV que se recibe como paramatro

    arg.
        nombre_archivo  nombre del CSV desde el cual se cargaran los datos iniciales de la lista de libros.
    """
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            #next(lector_csv)  # Saltar la cabecera
            for fila in lector_csv:
                titulo, autor, genero, puntuacion = fila
                nuevo_libro = Libro(titulo, autor, genero, float(puntuacion))
                lista_libros.append(nuevo_libro)
        print(f"Se han cargado {len(lista_libros)} libros desde el archivo '{nombre_archivo}'.\n")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'. Asegúrate de que exista en el directorio correcto.\n")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}\n")
    pausa()

def agregar_libro():
    """
    Solicita al usuario que ingrese el título, autor, género y puntuación del libro. 
    Crea un objeto Libro con estos atributos y agrega el objeto a la lista lista_libros.

    """
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    puntuacion = float(input("Ingrese la puntuación del libro (un número entre 0 y 10): "))
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado exitosamente.\n")

def buscar_libros_por_genero():
    """
    Pregunta al usuario por un género y muestra una lista de títulos de libros en ese género.

    """
    genero = input("Ingrese el género que desea buscar: ")
    libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_en_genero:
        print(f"Libros en el género '{genero}':")
        for libro in libros_en_genero:
            print(libro.titulo)
    else:
        print(f"No se encontraron libros en el género '{genero}'.\n")

def recomendar_libro():
    """
    Pregunta al usuario por su género de interés y muestra el título del libro con la puntuación más alta en ese género.

    """
    genero = input("Ingrese su género de interés: ")
    libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_en_genero:
        libro_recomendado = max(libros_en_genero, key=lambda libro: libro.puntuacion)
        print(f"Recomendación: '{libro_recomendado.titulo}' con una puntuación de {libro_recomendado.puntuacion}.\n")
    else:
        print(f"No se encontraron libros en el género '{genero}'.\n")

def listar_libros():
    """
    Muestra todos los libros almacenados en la lista lista_libros.

    """
    if lista_libros:
        print("Lista de todos los libros:\n")
        for libro in lista_libros:
            print(libro)
    else:
        print("No hay libros en la lista.\n")        

def listar_generos():
    """
    Muestra todos los géneros únicos en la lista de libros, ordenados alfabéticamente.

    """
    # Crear un conjunto para obtener géneros únicos
    generos_unicos = {libro.genero for libro in lista_libros}

    # Convertir el conjunto a una lista y ordenarla
    generos_ordenados = sorted(generos_unicos)

    if generos_ordenados:
        print("Géneros disponibles:\n")
        for genero in generos_ordenados:
            print(genero)
    else:
        print("No hay géneros disponibles en la lista de libros.\n")    

def menu():
    """
    Dibuja el Menu principal de la aplicacion
    
    """
    while True:             
        limpiar_pantalla()
        print(" ____________________________________ ")
        print("                                      ")
        print("| Sistema de Recomendacion de Libros |")                                
        print(" ____________________________________ ")
        print("")                
        print("Seleccione una opción:")
        print("")                
        print("1. Agregar Libro")
        print("2. Buscar Libros por Género")
        print("3. Recomendar Libro")
        print("")                
        print("R. Reinciar Listado de Libros")        
        print("L. Listar Libros")
        print("G. Listar Generos")
        print("")
        print("S. Salir")
        print("")
        opcion = input("Ingrese el número de la opción que desea realizar: ").upper()
        print("")
        print("")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libros_por_genero()
        elif opcion == "3":
            recomendar_libro()
        elif opcion == "R":
            refresh_libros()
        elif opcion == "L":
            listar_libros()
        elif opcion == "G":
            listar_generos()
        elif opcion == "S":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.\n")
        pausa()

def pausa():
    print("")
    print("Presione una tecla para continuar...")
    input()

def limpiar_pantalla():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/Mac
        os.system('clear')

# Cargar libros desde el archivo CSV al iniciar la aplicación
cargar_libros_desde_csv('libros.csv')

# Ejecutar el menú
menu()


    