import sqlite3

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect("videojuegos.db")

# Función para agregar un videojuego con manejo de transacciones
def agregar_videojuego():
    conexion = conectar()
    cursor = conexion.cursor()
    
    try:
        nombre = input("Introduce el nombre del videojuego: ")
        genero = input("Introduce el género del videojuego: ")
        ano_lanzamiento = int(input("Introduce el año de lanzamiento: "))
        id_desarrollador = int(input("Introduce el ID del desarrollador: "))

        cursor.execute('BEGIN TRANSACTION')  # Inicia la transacción
        cursor.execute('''
            INSERT INTO Videojuegos (Nombre, Genero, Ano_Lanzamiento, ID_Desarrollador) VALUES (?, ?, ?, ?)
        ''', (nombre, genero, ano_lanzamiento, id_desarrollador))
        conexion.commit()  # Guarda cambios si no hay errores

        print("✅ ¡Videojuego agregado con éxito!")

    except sqlite3.Error as e:
        conexion.rollback()  # Revierte los cambios en caso de error
        print(f"❌ Error al agregar el videojuego: {e}")

    finally:
        conexion.close()  # Cierra la conexión

# Función para consultar videojuegos
def consultar_videojuegos():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute('SELECT * FROM Videojuegos')
        videojuegos = cursor.fetchall()

        if videojuegos:
            print("\n📜 Lista de videojuegos:")
            for v in videojuegos:
                print(v)
        else:
            print("❌ No hay videojuegos registrados.")

    except sqlite3.Error as e:
        print(f"❌ Error al consultar videojuegos: {e}")

    finally:
        conexion.close()

# Función para modificar un videojuego con manejo de transacciones
def modificar_videojuego():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        id_videojuego = int(input("Introduce el ID del videojuego a modificar: "))
        nuevo_nombre = input("Introduce el nuevo nombre del videojuego: ")
        nuevo_genero = input("Introduce el nuevo género del videojuego: ")
        nuevo_ano_lanzamiento = int(input("Introduce el nuevo año de lanzamiento: "))
        nuevo_id_desarrollador = int(input("Introduce el nuevo ID del desarrollador: "))

        cursor.execute('BEGIN TRANSACTION')
        cursor.execute('''
            UPDATE Videojuegos 
            SET Nombre = ?, Genero = ?, Ano_Lanzamiento = ?, ID_Desarrollador = ? 
            WHERE ID_Videojuego = ?
        ''', (nuevo_nombre, nuevo_genero, nuevo_ano_lanzamiento, nuevo_id_desarrollador, id_videojuego))
        conexion.commit()

        print("✅ ¡Videojuego modificado con éxito!")

    except sqlite3.Error as e:
        conexion.rollback()
        print(f"❌ Error al modificar el videojuego: {e}")

    finally:
        conexion.close()

# Función para eliminar un videojuego con manejo de transacciones
def eliminar_videojuego():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        id_videojuego = int(input("Introduce el ID del videojuego a eliminar: "))
        
        cursor.execute('BEGIN TRANSACTION')
        cursor.execute('DELETE FROM Videojuegos WHERE ID_Videojuego = ?', (id_videojuego,))
        conexion.commit()

        print("✅ ¡Videojuego eliminado con éxito!")

    except sqlite3.Error as e:
        conexion.rollback()
        print(f"❌ Error al eliminar el videojuego: {e}")

    finally:
        conexion.close()

# Menú principal con navegación interactiva
def main():
    while True:
        print("\n🎮 MENÚ DE VIDEOJUEGOS INDIES")
        print("1️⃣ Agregar un videojuego")
        print("2️⃣ Consultar videojuegos")
        print("3️⃣ Modificar un videojuego")
        print("4️⃣ Eliminar un videojuego")
        print("5️⃣ Salir")

        try:
            opcion = int(input("🔹 Selecciona una opción: "))

            if opcion == 1:
                agregar_videojuego()
            elif opcion == 2:
                consultar_videojuegos()
            elif opcion == 3:
                modificar_videojuego()
            elif opcion == 4:
                eliminar_videojuego()
            elif opcion == 5:
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida, intenta de nuevo.")
        
        except ValueError:
            print("❌ Ingresa un número válido.")

if __name__ == "__main__":
    main()
