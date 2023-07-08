import mariadb
import sys

# Connect to MariaDB Platform
try:
    connection = mariadb.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        database="ParteA"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Crear un cursor para ejecutar consultas SQL
cursor = connection.cursor()

# Obtener información del medio de prensa
Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, year_fundation, url_principal = input("Indica la información del nuevo medio que quieres añadir con el formato siguiente: Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_Cobertura, id_prensa, year_fundation, url_principal -> ").split(", ")

PrensaArray = [Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, year_fundation, url_principal]

cursor.execute("INSERT INTO prensa (Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, year_fundation, url_principal) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(PrensaArray[0], PrensaArray[1], PrensaArray[2], PrensaArray[3], PrensaArray[4], PrensaArray[5], PrensaArray[6], PrensaArray[7]))

connection.commit()
connection.close()

print("-------------------------------------------------------")
print("------------------> MEDIO DE PRENSA <------------------")
print("----------------> AGREGADO CON EXTIO! <----------------")
print("-------------------------------------------------------")


def leeArchivo(archivo):
    emoticons = []
    text_emoticons = open('emoticons.txt','r')

    #Se genera lista con los emoticones y sus respectivo nombres
    for e in text_emoticons:
        linea = e.strip() #Aien\n -> Alien
        linea = linea.split(", ") # "(.V.) Alien" --> ["(.V.)", "Alien"] .... 
        emoticons.append(linea)

    #Se remplazan los guiones del nombre del emoticon y se transforma en mayusculas
    for i in range (len(emoticons)):
        emoticons[i][1] = emoticons[i][1].replace("-"," ")
        emoticons[i][1] = emoticons[i][1].upper()