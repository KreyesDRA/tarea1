import sqlite3

# Función para validar que un campo contiene solo letras
def validar_letras(campo):
    if campo.isalpha():
        return True
    else:
        print("Error: El campo debe contener solo letras.")
        return False

# Función para validar que un campo contiene solo números
def validar_numeros(campo):
    if campo.isdigit():
        return True
    else:
        print("Error: El campo debe contener solo números.")
        return False

# Función para ingresar y validar información personal
def ingresar_informacion():
    nombre = input("Ingrese el nombre: ")
    while not validar_letras(nombre):
        nombre = input("Ingrese el nombre: ")

    segundo_nombre = input("Ingrese el segundo nombre: ")
    while not validar_letras(segundo_nombre):
        segundo_nombre = input("Ingrese el segundo nombre: ")

    apellido = input("Ingrese el apellido: ")
    while not validar_letras(apellido):
        apellido = input("Ingrese el apellido: ")

    segundo_apellido = input("Ingrese el segundo apellido: ")
    while not validar_letras(segundo_apellido):
        segundo_apellido = input("Ingrese el segundo apellido: ")

    cedula = input("Ingrese la cédula: ")
    while not validar_numeros(cedula):
        cedula = input("Ingrese la cédula: ")

    telefono = input("Ingrese el teléfono: ")
    while not validar_numeros(telefono):
        telefono = input("Ingrese el teléfono: ")

    nacionalidad = input("Ingrese la nacionalidad: ")
    while not validar_letras(nacionalidad):
        nacionalidad = input("Ingrese la nacionalidad: ")

    trabajo = input("Ingrese en qué trabaja: ")

    return (nombre, segundo_nombre, apellido, segundo_apellido, cedula, telefono, nacionalidad, trabajo)

# Función para crear la tabla SQLite e ingresar datos
def crear_tabla_y_registrar_datos():
    conn = sqlite3.connect('diccionario.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            segundo_nombre TEXT,
            apellido TEXT,
            segundo_apellido TEXT,
            cedula TEXT,
            telefono TEXT,
            nacionalidad TEXT,
            trabajo TEXT
        )
    ''')

    while True:
        informacion = ingresar_informacion()

        cursor.execute('''
            INSERT INTO personas (nombre, segundo_nombre, apellido, segundo_apellido, cedula, telefono, nacionalidad, trabajo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', informacion)

        conn.commit()

        respuesta = input("¿Desea ingresar otra persona? (S/N): ")
        if respuesta.lower() != 's':
            break

    conn.close()

if __name__ == "__main__":
    crear_tabla_y_registrar_datos()
