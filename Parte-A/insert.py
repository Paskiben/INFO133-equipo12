import mariadb;
import sys;

# Conectarse a la base de datos
try: 
    conexion = mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="contraseña",
        database="EQUIPO12"
    )

except mariadb.Error as e:
    print("Ha sucedido un error al conectarse a Mariadb, intente nuevamente")
    sys.exit(1)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Obtener información del usuario
nombre, ciudad, region, pais, continente, ano_creacion = input("Indica la información del nuevo medio que quieres añadir con el formato siguiente: nombre, ciudad, region, pais, continente, año de creación: ").split(",")

url_noticia = input("Indica una URL de una noticia de este medio: ")
xpath_titulo = input("Indica la expresión XPATH que permite leer el título de la fecha: ")

# Insertar el nuevo medio en la base de datos
query = "INSERT INTO medios_prensa (nombre, ciudad, region, pais, continente, ano_creacion, url_noticia, xpath_titulo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
values = (nombre.strip(), ciudad.strip(), region.strip(), pais.strip(), continente.strip(), ano_creacion.strip(), url_noticia.strip(), xpath_titulo.strip())

cursor.execute(query, values)

# Confirmar los cambios y cerrar la conexión a la base de datos
conexion.commit()
conexion.close()

print("El medio de prensa se ha insertado exitosamente en la base de datos.")
