import sqlite3  # Importa la librería sqlite3 para manejar la base de datos

# Lista de videojuegos indies
videojuegos = [
    (1, 'Hollow Knight', 'Metroidvania', 2017, 1),
    (2, 'Celeste', 'Plataformas', 2018, 2),
    (3, 'Undertale', 'RPG', 2015, 3),
    (4, 'Stardew Valley', 'Simulación', 2016, 4),
    (5, 'Hades', 'Roguelike', 2020, 5),
    (6, 'Cuphead', 'Run and Gun', 2017, 6),
    (7, 'Outer Wilds', 'Aventura', 2019, 7),
    (8, 'Slay the Spire', 'Cartas/Roguelike', 2017, 8),
    (9, 'Dead Cells', 'Roguelike/Metroidvania', 2018, 9),
    (10, 'Disco Elysium', 'RPG', 2019, 10)
]

# Lista de desarrolladores
desarrolladores = [
    (1, 'Team Cherry', 'Australia'),
    (2, 'Maddy Makes Games', 'Canadá'),
    (3, 'Toby Fox', 'Estados Unidos'),
    (4, 'ConcernedApe', 'Estados Unidos'),
    (5, 'Supergiant Games', 'Estados Unidos'),
    (6, 'Studio MDHR', 'Canadá'),
    (7, 'Mobius Digital', 'Estados Unidos'),
    (8, 'MegaCrit Games', 'Estados Unidos'),
    (9, 'Motion Twin', 'Francia'),
    (10, 'ZA/UM', 'Estonia')
]

# Lista de compras de videojuegos
compras = [
    (1, 1, '2023-01-05', 2, 40.00),
    (2, 2, '2023-02-10', 1, 20.00),
    (3, 3, '2023-03-15', 5, 100.00),
    (4, 4, '2023-04-20', 3, 60.00),
    (5, 5, '2023-05-10', 4, 80.00),
    (6, 6, '2023-06-25', 1, 20.00),
    (7, 7, '2023-07-15', 2, 40.00),
    (8, 8, '2023-08-05', 3, 60.00),
    (9, 9, '2023-09-10', 2, 40.00),
    (10, 10, '2023-10-20', 1, 20.00)
]

# Conecta o crea la base de datos
conexion = sqlite3.connect("videojuegos.db")
cursor = conexion.cursor()

# Crea la tabla Desarrolladores
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Desarrolladores (
    ID_Desarrollador INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Pais_Origen VARCHAR(255)
);
''')

# Crea la tabla Videojuegos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Videojuegos (
    ID_Videojuego INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Genero VARCHAR(100),
    Ano_Lanzamiento INT,
    ID_Desarrollador INT,
    FOREIGN KEY (ID_Desarrollador) REFERENCES Desarrolladores(ID_Desarrollador) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE
);
''')

# Crea la tabla Compras
cursor.execute('''
CREATE TABLE IF NOT EXISTS Compras (
    ID_Compra INT PRIMARY KEY,
    ID_Videojuego INT,
    Fecha_Compra DATE,
    Cantidad_Comprados INT,
    Precio_Total DECIMAL(10, 2),
    FOREIGN KEY (ID_Videojuego) REFERENCES Videojuegos(ID_Videojuego) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE
);
''')

# Inserta datos en la tabla Desarrolladores
cursor.executemany('''
INSERT INTO Desarrolladores (ID_Desarrollador, Nombre, Pais_Origen) VALUES (?, ?, ?)
''', desarrolladores)

# Inserta datos en la tabla Videojuegos
cursor.executemany('''          
INSERT INTO Videojuegos (ID_Videojuego, Nombre, Genero, Ano_Lanzamiento, ID_Desarrollador) VALUES (?, ?, ?, ?, ?)
''', videojuegos)     

# Inserta datos en la tabla Compras
cursor.executemany ('''              
INSERT INTO Compras (ID_Compra, ID_Videojuego, Fecha_Compra, Cantidad_Comprados, Precio_Total) VALUES (?, ?, ?, ?, ?)
''', compras) 

# Guarda los cambios y cierra la conexión
conexion.commit()
conexion.close()
