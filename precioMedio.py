import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

def obtener_fecha(nombre_archivo):
    # Extraer la fecha del nombre del archivo
    fecha_str = nombre_archivo.replace('Reporte ', '').replace('.csv', '')
    fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
    return fecha

def calcular_promedio_precios(archivo_csv):
    total_precios = 0
    num_precios = 0
    
    with open(archivo_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            precio_str = row['price']
            
            if precio_str:  # Verificar si la cadena de precio no está vacía
                precio_str = precio_str.replace('$', '')  # Eliminar el símbolo de moneda
                precio = float(precio_str)
                total_precios += precio
                num_precios += 1
    
    if num_precios > 0:
        promedio = total_precios / num_precios
        return promedio
    else:
        return 0

# Ruta de la carpeta que contiene los archivos CSV
ruta_carpeta = r'C:\Repo Prueba\Fshop\Reportes'

archivos_csv = os.listdir(ruta_carpeta)  # Obtener la lista de archivos en la carpeta

# Ordenar los archivos CSV por fecha
archivos_csv_ordenados = sorted(archivos_csv, key=obtener_fecha)

fechas = []  # Lista para almacenar las fechas
promedios = []  # Lista para almacenar los precios promedio

for archivo in archivos_csv_ordenados:
    if archivo.endswith('.csv'):
        archivo_csv = os.path.join(ruta_carpeta, archivo)
        promedio = calcular_promedio_precios(archivo_csv)
        fecha = obtener_fecha(archivo)
        
        fechas.append(fecha)
        promedios.append(promedio)
        
# Graficar la evolución del precio promedio
plt.plot(fechas, promedios)
plt.xlabel('Fecha')
plt.ylabel('Precio promedio')
plt.title('Evolución del precio promedio')
plt.xticks(rotation=45)
plt.show()
