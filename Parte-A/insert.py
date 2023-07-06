import mariadb;
import sys;

# Conectarse a la base de datos
try: 
    conexion = mariadb.connect(
        host="localhost",
        user="root",
        password="123456",
        database="parteB"
    )

except mariadb.Error as e:
    print("Ha sucedido un error al conectarse a Mariadb, intente nuevamente")
    sys.exit(1)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Obtener información del medio de prensa
Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, id_prensa, year_fundation, url_principal = input("Indica la información del nuevo medio que quieres añadir con el formato siguiente: Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_Cobertura, id_prensa, year_fundation, url_principal").split(",")

url_noticia = input("Indica una URL de una noticia de este medio: ")
xpath_titulo = input("Indica la expresión XPATH que permite leer el título de la fecha: ")

cur.execute("INSERT INTO Prensa (Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, id_prensa, year_fundation, url_principal) VALUES (?, ?, ?, ?, ?, ?)",(infoArray[4], infoArray[5], infoArray[0], infoArray[2], infoArray[3], infoArray[1]))

# Insertar el nuevo medio en la base de datos
query = "INSERT INTO medios_prensa (nombre, ciudad, region, pais, continente, ano_creacion, url_noticia, xpath_titulo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
values = (nombre.strip(), ciudad.strip(), region.strip(), pais.strip(), continente.strip(), ano_creacion.strip(), url_noticia.strip(), xpath_titulo.strip())

cursor.execute(query, values)

# Confirmar los cambios y cerrar la conexión a la base de datos
conexion.commit()
conexion.close()

print("El medio de prensa se ha insertado exitosamente en la base de datos.")
