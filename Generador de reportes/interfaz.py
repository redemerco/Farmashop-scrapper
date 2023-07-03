import tkinter as tk
from tkinter import ttk
import subprocess

def ejecutar_script(script_path):
    subprocess.run(["python", script_path])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Farmashop Scrapper")

# Crear el estilo
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)

# Funciones para ejecutar los scripts
def ejecutar_densidad_de_precios_hoy():
    script_path = r"C:\Repo Prueba\Fshop\Generador de reportes\densidadDePreciosHoy.py"
    ejecutar_script(script_path)

def ejecutar_evolucion_precio_medio():
    script_path = r"C:\Repo Prueba\Fshop\Generador de reportes\evolucionPrecioMedio.py"
    ejecutar_script(script_path)

def ejecutar_evolucion_precio_producto():
    script_path = r"C:\Repo Prueba\Fshop\Generador de reportes\evolucionPrecioProducto.py"
    ejecutar_script(script_path)

def ejecutar_productos_agregados_hoy():
    script_path = r"C:\Repo Prueba\Fshop\Generador de reportes\productosAgregadosHoy.py"
    ejecutar_script(script_path)

def ejecutar_todos_los_productos():
    script_path = r"C:\Repo Prueba\Fshop\Generador de reportes\todosLosProductos.py"
    ejecutar_script(script_path)

def ejecutar_fvck_farmashop():
    script_path = r"C:\Repo Prueba\Fshop\fvckFarmashop.py"
    ejecutar_script(script_path)

def ejecutar_topQuinientosMasCaros():
    script_path = r"C:\Repo Prueba\Fshop\Generador de reportes\topQuinientosMasCarosHoy.py"
    ejecutar_script(script_path)

# Crear los botones con estilo
boton_densidad_de_precios_hoy = ttk.Button(ventana, text="Densidad de Precios Hoy", command=ejecutar_densidad_de_precios_hoy)
boton_evolucion_precio_medio = ttk.Button(ventana, text="Evolución Precio Medio", command=ejecutar_evolucion_precio_medio)
boton_evolucion_precio_producto = ttk.Button(ventana, text="Evolución Precio Producto", command=ejecutar_evolucion_precio_producto)
boton_productos_agregados_hoy = ttk.Button(ventana, text="Productos Agregados Hoy", command=ejecutar_productos_agregados_hoy)
boton_todos_los_productos = ttk.Button(ventana, text="Todos los Productos", command=ejecutar_todos_los_productos)
boton_fvck_farmashop = ttk.Button(ventana, text="Scrappear productos", command=ejecutar_fvck_farmashop)
boton_top_Quinientos_Mas_caros_hoy = ttk.Button(ventana, text="Top 500 productos mas caros", command=ejecutar_topQuinientosMasCaros)

# Colocar los botones en la ventana
boton_densidad_de_precios_hoy.pack(pady=10)
boton_evolucion_precio_medio.pack(pady=10)
boton_evolucion_precio_producto.pack(pady=10)
boton_productos_agregados_hoy.pack(pady=10)
boton_top_Quinientos_Mas_caros_hoy.pack(pady=10)
boton_todos_los_productos.pack(pady=10)
boton_fvck_farmashop.pack(pady=10)
# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
