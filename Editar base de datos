import sqlite3

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect("videojuegos.db")

# Función para agregar un videojuego
def agregar_videojuego():
    conexion = conectar()
    cursor = conexion.cursor()

    nombre = input("Introduce el nombre del videojuego: ")
    genero = input("Introduce el género del videojuego: ")
    ano_lanzamiento = int(input("Introduce el año de lanzamiento: "))
    id_desarrollador = int(input("Introduce el ID del desarrollador: "))

    cursor.execute('''
        INSERT INTO Videojuegos (Nombre, Genero, Ano_Lanzamiento, ID_Desarrollador) VALUES (?, ?, ?, ?)
    ''', (nombre, genero, ano_lanzamiento, id_desarrollador))

    conexion.commit()
    conexion.close()
    print("¡Videojuego agregado con éxito!")

# Función para consultar videojuegos
def consultar_videojuegos():
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('SELECT * FROM Videojuegos')
    videojuegos = cursor.fetchall()

    if videojuegos:
        for v in videojuegos:
            print(v)
    else:
        print("No hay videojuegos registrados.")

    conexion.close()

# Función para modificar un videojuego
def modificar_videojuego():
    conexion = conectar()
    cursor = conexion.cursor()

    id_videojuego = int(input("Introduce el ID del videojuego a modificar: "))
    nuevo_nombre = input("Introduce el nuevo nombre del videojuego: ")
    nuevo_genero = input("Introduce el nuevo género del videojuego: ")
    nuevo_ano_lanzamiento = int(input("Introduce el nuevo año de lanzamiento: "))
    nuevo_id_desarrollador = int(input("Introduce el nuevo ID del desarrollador: "))

    cursor.execute('''
        UPDATE Videojuegos 
        SET Nombre = ?, Genero = ?, Ano_Lanzamiento = ?, ID_Desarrollador = ? 
        WHERE ID_Videojuego = ?
    ''', (nuevo_nombre, nuevo_genero, nuevo_ano_lanzamiento, nuevo_id_desarrollador, id_videojuego))

    conexion.commit()
    conexion.close()
    print("¡Videojuego modificado con éxito!")

# Función para eliminar un videojuego
def eliminar_videojuego():
    conexion = conectar()
    cursor = conexion.cursor()

    id_videojuego = int(input("Introduce el ID del videojuego a eliminar: "))
    
    cursor.execute('DELETE FROM Videojuegos WHERE ID_Videojuego = ?', (id_videojuego,))
    
    conexion.commit()
    conexion.close()
    print("¡Videojuego eliminado con éxito!")

# Menú principal
def main():
    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Agregar un videojuego")
        print("2. Consultar videojuegos")
        print("3. Modificar un videojuego")
        print("4. Eliminar un videojuego")
        print("5. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            agregar_videojuego()
        elif opcion == 2:
            consultar_videojuegos()
        elif opcion == 3:
            modificar_videojuego()
        elif opcion == 4:
            eliminar_videojuego()
        elif opcion == 5:
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
