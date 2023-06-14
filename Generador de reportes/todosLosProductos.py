import os
import pandas as pd
import shutil

# Ruta del directorio que contiene los archivos CSV
directorio = "C:\\Repo Prueba\\Fshop\\Reportes"

# Lista para almacenar los datos de todos los archivos CSV
datos_totales = []

# Recorrer los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".csv"):
        # Ruta completa del archivo
        ruta_archivo = os.path.join(directorio, archivo)
        
        # Leer el archivo CSV y agregar los datos a la lista
        datos_csv = pd.read_csv(ruta_archivo)
        datos_totales.append(datos_csv)

# Combinar los datos de todos los archivos en un único DataFrame
datos_combinados = pd.concat(datos_totales, ignore_index=True)

# Eliminar duplicados basados en la columna 'sku'
datos_combinados_sin_duplicados = datos_combinados.drop_duplicates(subset='sku')

# Guardar los datos sin duplicados en un nuevo archivo CSV
ruta_salida = os.path.join(directorio, "todosLosProductos.csv")
datos_combinados_sin_duplicados.to_csv(ruta_salida, index=False)

# Mover el archivo a la nueva ubicación
ruta_destino = "C:\\Repo Prueba\\Fshop\\todosLosProductos.csv"
shutil.move(ruta_salida, ruta_destino)

print("Se ha generado el archivo 'todosLosProductos.csv' sin duplicados y se ha movido a la ruta 'C:\\Repo Prueba\\Fshop'.")
