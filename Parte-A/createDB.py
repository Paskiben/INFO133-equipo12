import mariadb
import sys

# Connect to MariaDB Platform
try:
    connection = mariadb.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        port=3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = connection.cursor()

# Crear base de datos
try:
    cursor.execute("CREATE DATABASE ParteA")
except mariadb.ProgrammingError:
    print("La Base de Datos ha sido creada")

# Usar base de datos 
cursor.execute("USE ParteA")
try:
    cursor.execute("DROP TABLE prensa")
    cursor.execute("DROP TABLE fundadores")
    cursor.execute("DROP TABLE noticia")
    cursor.execute("DROP TABLE categoria")
    cursor.execute("DROP TABLE red_social")
except: pass
# Crear tablas
cursor.execute(
    """CREATE TABLE IF NOT EXISTS prensa(
        Pais VARCHAR(50),
        Continente VARCHAR(50), 
        Region VARCHAR(50),
        Ciudad VARCHAR(50),
        Nombre_prensa VARCHAR(50),
        Tipo_cobertura VARCHAR(50),
        id_prensa INT NOT NULL AUTO_INCREMENT,
        year_fundation YEAR,
        url_principal VARCHAR(900),
        PRIMARY KEY(id_prensa)
    )""")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS fundadores(
        Nombre_fundadores VARCHAR(50),
        id_fundadores INT NOT NULL AUTO_INCREMENT,
        id_prensa INT,
        PRIMARY KEY(id_fundadores),
        FOREIGN KEY(id_prensa) REFERENCES prensa (id_prensa)
    )""")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS noticia(
        xpath_titulo VARCHAR(50),
        xpath_contenido VARCHAR(50),
        xpath_fecha VARCHAR(50),
        url_noticia VARCHAR(900),
        id_noticia INT NOT NULL AUTO_INCREMENT,
        id_prensa INT,
        PRIMARY KEY(id_noticia),
        FOREIGN KEY(id_prensa) REFERENCES prensa (id_prensa)
    )""")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS categoria(
        xpath_categoria VARCHAR(50),
        url_categoria VARCHAR(900),
        id_categoria INT NOT NULL AUTO_INCREMENT,
        id_prensa INT,
        PRIMARY KEY(id_categoria),
        FOREIGN KEY(id_prensa) REFERENCES prensa (id_prensa) 
    )""")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS red_social(
        nombre_red_social VARCHAR(50),
        id_red_social INT NOT NULL AUTO_INCREMENT,
        seguidores INT,
        id_prensa INT,
        PRIMARY KEY(id_red_social),
        FOREIGN KEY(id_prensa) REFERENCES prensa (id_prensa) 
    )""")
