import pandas as pd

# Cargar el archivo CSV en un DataFrame
ruta_csv = r'C:\Repo Prueba\Fshop\fijo.csv'
df = pd.read_csv(ruta_csv)

# Eliminar el signo de dólar y el separador de miles de la columna 'price'
df['price'] = df['price'].str.replace('$', '')
df['price'] = df['price'].str.replace('.', '').astype(int)

# Ordenar el DataFrame por la columna 'price' en orden descendente
df = df.sort_values('price', ascending=False)

# Tomar solo las primeras 500 filas
df = df.head(500)

# Guardar el DataFrame con las primeras 500 filas en un nuevo archivo CSV
ruta_csv_ordenado = r'C:\Repo Prueba\Fshop\topQuinientosMasCarosHoy.csv'
df.to_csv(ruta_csv_ordenado, index=False)
print("Se ha generado el archivo 'topQuinientosMasCarosHoy.csv' sin duplicados y se ha movido a la ruta 'C:\\Repo Prueba\\Fshop'.")
