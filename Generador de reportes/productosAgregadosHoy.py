import os
import csv
import pandas as pd

def obtener_fecha_creacion(archivo):
    nombre_archivo = archivo.split(' ')[1].split('.')[0]
    dia, mes, anio = map(int, nombre_archivo.split('-'))
    return anio, mes, dia

directorio = r'C:\Repo Prueba\Fshop\Reportes'
extension = '.csv'

archivos_csv = [archivo for archivo in os.listdir(directorio) if archivo.endswith(extension)]

archivo_mas_reciente = None
fecha_mas_reciente = None

for archivo in archivos_csv:
    fecha_archivo = obtener_fecha_creacion(archivo)
    if fecha_mas_reciente is None or fecha_archivo > fecha_mas_reciente:
        fecha_mas_reciente = fecha_archivo
        archivo_mas_reciente = archivo

lista_sku_archivo_fijo = []
lista_sku_archivo_mas_reciente = []

ruta_archivo_mas_reciente = os.path.join(directorio, archivo_mas_reciente)
ruta_archivo_fijo = os.path.join(r"C:\Repo Prueba\Fshop", 'fijo.csv')

# Leer el archivo fijo
with open(ruta_archivo_fijo, 'r', newline='', encoding='utf-8') as archivo_fijo_csv:
    lector_fijo_csv = csv.reader(archivo_fijo_csv)
    next(lector_fijo_csv)  # Omitir la primera línea del archivo (encabezados)
    
    for linea in lector_fijo_csv:
        sku = linea[0]
        lista_sku_archivo_fijo.append(sku)

# Leer el archivo más reciente
with open(ruta_archivo_mas_reciente, 'r', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Omitir la primera línea del archivo (encabezados)
    
    for linea in lector_csv:
        sku = linea[0]
        lista_sku_archivo_mas_reciente.append(sku)

skus_novedades = set(lista_sku_archivo_fijo) - set(lista_sku_archivo_mas_reciente)

# Crear DataFrame con los SKU, nombres y precios
df_novedades = pd.DataFrame(columns=["sku", "nombre", "precio"])

for sku in skus_novedades:
    # Buscar SKU en el archivo fijo
    with open(ruta_archivo_fijo, 'r', newline='', encoding='utf-8') as archivo_fijo_csv:
        lector_fijo_csv = csv.reader(archivo_fijo_csv)
        next(lector_fijo_csv)  # Omitir la primera línea del archivo (encabezados)
        
        for linea in lector_fijo_csv:
            if linea[0] == sku:
                nombre = linea[1]
                precio = linea[2]
                df_novedades = pd.concat([df_novedades, pd.DataFrame({"sku": [sku], "nombre": [nombre], "precio": [precio]})], ignore_index=True)
                break

# Eliminar filas vacías del DataFrame
df_novedades.dropna(subset=["sku", "nombre", "precio"], how='all', inplace=True)
realdf= df_novedades.drop_duplicates(subset='sku')
# Guardar el DataFrame en un archivo CSV
realdf.to_csv("C:/Repo Prueba/Fshop/productosAgregadosHoy.csv", index=False)
print("Se ha generado el archivo 'productosAgregadosHoy.csv' sin duplicados y se ha movido a la ruta 'C:\Repo Prueba\Fshop'")