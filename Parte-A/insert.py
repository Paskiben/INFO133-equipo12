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
Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, id_prensa, year_fundation, url_principal = input("Indica la información del nuevo medio que quieres añadir con el formato siguiente: Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_Cobertura, id_prensa, year_fundation, url_principal -> ").split(", ")

PrensaArray = [Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, id_prensa, year_fundation, url_principal]

cursor.execute("INSERT INTO prensa (Pais, Continente, Region, Ciudad, Nombre_Prensa, Tipo_cobertura, id_prensa, year_fundation, url_principal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(PrensaArray[0], PrensaArray[1], PrensaArray[2], PrensaArray[3], PrensaArray[4], PrensaArray[5], PrensaArray[6], PrensaArray[7], PrensaArray[8]))

connection.commit()
connection.close()

print("-------------------------------------------------------")
print("------------------> MEDIO DE PRENSA <------------------")
print("----------------> AGREGADO CON EXTIO! <----------------")
print("-------------------------------------------------------")
