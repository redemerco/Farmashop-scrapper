import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Obtener la ruta de la carpeta que contiene los archivos CSV
carpeta_csv = r'C:\Repo Prueba\Fshop\Reportes'

# Obtener el SKU del usuario
sku_buscar = input("Ingresa el SKU a buscar: ")

# Diccionario para almacenar el precio más reciente por fecha
precios_por_fecha = {}

# Recorrer todos los archivos CSV en la carpeta
for archivo in os.listdir(carpeta_csv):
    if archivo.endswith('.csv'):
        ruta_archivo = os.path.join(carpeta_csv, archivo)
        
        # Obtener la fecha del nombre del archivo
        nombre_archivo = os.path.splitext(archivo)[0]  # Eliminar la extensión .csv
        fecha_str = nombre_archivo.split(' ')[1]  # Obtener la parte de la fecha en el nombre del archivo
        fecha = datetime.strptime(fecha_str, '%d-%m-%Y').date()
        
        # Abrir el archivo CSV
        with open(ruta_archivo, 'r', encoding="UTF-8") as csv_file:
            reader = csv.DictReader(csv_file)
            
            # Buscar el SKU en el archivo actual
            for row in reader:
                if row['sku'] == sku_buscar:
                    precio = float(row['price'].replace('$', '').replace(".",""))
                    
                    # Actualizar el precio más reciente para la fecha actual
                    if fecha not in precios_por_fecha or fecha > max(precios_por_fecha.keys()):
                        precios_por_fecha[fecha] = precio

# Ordenar las fechas y los precios por fecha
fechas_ordenadas = sorted(precios_por_fecha.keys())
precios_ordenados = [precios_por_fecha[fecha] for fecha in fechas_ordenadas]

# Crear el gráfico de línea
plt.plot(fechas_ordenadas, precios_ordenados)
plt.title(f"Evolución del precio del SKU {sku_buscar}")
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
