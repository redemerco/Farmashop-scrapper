import csv
import matplotlib.pyplot as plt

# Ruta del archivo CSV
file_path = r'C:\Repo Prueba\Fshop\fijo.csv'

# Leer el archivo CSV y obtener los precios de los productos
prices = []
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        price_str = row['price'].replace('$', '').replace('.', '')
        if price_str:
            price = float(price_str)
            prices.append(price)

# Calcular la diferencia entre el precio más alto y el precio más bajo
max_price = max(prices)
min_price = min(prices)
price_difference = max_price - min_price

# Dividir el resultado entre 5
result = price_difference / 100

# Definir los límites de precios
lower_limit = result
upper_limit = result * 100

# Contadores de productos por rango de precios
contadores = {}

# Leer el archivo CSV y contar los productos en cada rango de precios
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        precio_str = row['price'].replace('$', '').replace('.', '')
        if precio_str:
            precio = float(precio_str)
            for i in range(1, 101):
                if lower_limit * i < precio < upper_limit * i:
                    if i not in contadores:
                        contadores[i] = 1
                    else:
                        contadores[i] += 1

# Crear una lista de valores y etiquetas para el gráfico
valores = list(contadores.values())
etiquetas = list(contadores.keys())

# Crear el gráfico de barras
plt.bar(etiquetas, valores)
plt.xlabel('Rango de precios')
plt.ylabel('Cantidad de productos')
plt.title('Contadores de productos por rango de precios')

# Mostrar el gráfico
plt.show()

