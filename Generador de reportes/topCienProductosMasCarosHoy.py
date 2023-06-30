import pandas as pd

# Ruta del archivo CSV
csv_path = r'C:\Repo Prueba\Fshop\fijo.csv'

# Lee el archivo CSV y convierte la columna "sku" en cadenas de texto
df = pd.read_csv(csv_path, dtype={'sku': str})

# Ordena el DataFrame por precio de forma descendente
df_sorted = df.sort_values('price', ascending=False)

# Selecciona los 100 productos más caros
top_100 = df_sorted.head(100)

# Elimina el ".0" al final de los valores de la columna "sku"
top_100['sku'] = top_100['sku'].str.rstrip('.0')

# Elimina los caracteres no numéricos de la columna "price"
top_100['price'] = top_100['price'].replace('.', '', regex=True).replace('$', '', regex=True)

# Convierte la columna "price" a valores numéricos
top_100['price'] = pd.to_numeric(top_100['price'])

# Convierte los valores de precio a formato de cadena de texto sin cambios
top_100['price'] = top_100['price'].apply(lambda x: f"{x:.3f}")

# Guarda los resultados en un nuevo archivo CSV
top_100.to_csv('top_100_mas_caros.csv', index=False)
