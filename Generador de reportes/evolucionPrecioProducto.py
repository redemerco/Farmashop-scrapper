import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Obtener la ruta de la carpeta que contiene los archivos CSV
carpeta_csv = r'C:\Repo Prueba\Fshop\Reportes'

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Buscar SKU")

# Configurar estilos de la ventana
ventana.configure(bg="#F0F0F0")
ventana.geometry("300x150")

# Función para procesar la entrada del SKU
def buscar_sku():
    sku_buscar = entrada_sku.get()
    if sku_buscar:
        ventana.destroy()  # Cerrar la ventana
        generar_grafico(sku_buscar)
    else:
        messagebox.showerror("Error", "Por favor ingresa un SKU válido.")

# Estilo para etiquetas
estilo_etiqueta = ttk.Style()
estilo_etiqueta.configure("EstiloEtiqueta.TLabel", foreground="#333333", background="#F0F0F0", font=("Arial", 12, "bold"))

# Etiqueta y campo de entrada para el SKU
etiqueta_sku = ttk.Label(ventana, text="SKU a buscar:", style="EstiloEtiqueta.TLabel")
etiqueta_sku.pack(pady=10)
entrada_sku = ttk.Entry(ventana, font=("Arial", 12))
entrada_sku.pack()

# Botón para buscar el SKU
boton_buscar = ttk.Button(ventana, text="Buscar", command=buscar_sku)
boton_buscar.pack(pady=10)

# Función para generar el gráfico
def generar_grafico(sku_buscar):
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
                        precio = float(row['price'].replace('$', '').replace(".", ""))

                        # Actualizar el precio más reciente para la fecha actual
                        if fecha not in precios_por_fecha or fecha > max(precios_por_fecha.keys()):
                            precios_por_fecha[fecha] = precio

    # Verificar si se encontraron precios para el SKU
    if not precios_por_fecha:
        messagebox.showerror("Error", f"No se encontraron registros para el SKU {sku_buscar}")
        return

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

# Iniciar la ejecución de la ventana principal
ventana.mainloop()
