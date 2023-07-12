import shutil
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures
from requests_futures.sessions import FuturesSession
import csv
from tqdm import tqdm
import datetime
import os

def get_product_data(response, main_url):
    product_data = {}
    soup = BeautifulSoup(response.content, "html.parser")
    textSku = soup.find('div', class_="product attribute sku")
    if textSku is not None:
        product_data['sku'] = textSku.get_text().replace("\nSKU\n", "").replace("\n", "")
    else:
        product_data['sku'] = ""
    textName = soup.find('span', class_="base")
    if textName is not None:
        product_data['name'] = textName.get_text().replace("\xa0", "")
    else:
        product_data['name'] = ""
    textPrice = soup.find('span', class_="price-wrapper")
    if textPrice is not None:
        product_data['price'] = textPrice.get_text().replace("\xa0", "")
    else:
        product_data['price'] = ""
    product_data['main_url'] = main_url
    return product_data

def get_product_urls(response):
    soup = BeautifulSoup(response.content, "html.parser")
    product_urls = []
    for i in soup.find_all('a', class_="product-item-link", href=True):
        product_urls.append(i['href'])
    return product_urls

def get_main_urls(response):
    soup = BeautifulSoup(response.content, "html.parser")
    main_urls = []
    for i in soup.find_all("a", class_="nav-anchor", href=True):
        main_urls.append(i['href'].replace("#", "https://tienda.farmashop.com.uy/"))
        main_urls =list(dict.fromkeys(main_urls))
    return main_urls

def scrape_website(url):
    product_urls = []
    session = FuturesSession()
    future_main_urls = session.get(url)
    main_urls = get_main_urls(future_main_urls.result())
    future_to_url = {session.get(url): url for url in main_urls}
    for future in tqdm(concurrent.futures.as_completed(future_to_url), total=len(future_to_url), desc="Getting product URLs"):
        try:
            product_urls.extend(get_product_urls(future.result()))
        except Exception as exc:
            print('generated an exception: %s' % exc)
    products_data = []
    future_to_url = {session.get(url): url for url in product_urls}
    for future in tqdm(concurrent.futures.as_completed(future_to_url), total=len(future_to_url), desc="Scraping products"):
        try:
            main_url = future_to_url[future]
            products_data.append(get_product_data(future.result(), main_url))
        except Exception as exc:
            print('generated an exception: %s' % exc)
    df = pd.DataFrame(products_data, columns=['sku', 'name', 'price'])
    df.to_csv('variable.csv', index=False)
    
scrape_website("https://tienda.farmashop.com.uy/")
archivo_1 = "fijo.csv"
archivo_2 = "variable.csv"
archivo_salida = "diferencias.csv"
with open(archivo_1, "r", encoding='utf-8') as f1, open(archivo_2, "r", encoding='utf-8') as f2, open(archivo_salida, "w", newline="", encoding='utf-8') as fsalida:
    lector1 = csv.reader(f1)
    lector2 = csv.reader(f2)
    escritor = csv.writer(fsalida)
    precios = {}
    skus_escritos = set()  # conjunto para almacenar los SKUs ya escritos
    for row in lector2:
        precios[row[0]] = row[2]
    for row in lector1:
        sku = row[0]
        precio_1 = row[2]
        precio_2 = precios.get(sku, "Sin datos")
        if precio_2 == "Sin datos":
            continue  # skip writing if precio_2 is "Sin datos"
        if precio_1 != precio_2 and sku not in skus_escritos:
            escritor.writerow([sku, precio_1, precio_2]) 
            skus_escritos.add(sku)  # añadir el SKU a la lista de SKUs escritos, 
fecha_actual = datetime.datetime.now().strftime('%d-%m-%Y')
nombre_archivo_actual = 'fijo.csv'
nombre_archivo_nuevo = "Reporte "f'{fecha_actual}.csv'
os.rename(nombre_archivo_actual, nombre_archivo_nuevo)
os.rename("variable.csv", "fijo.csv")
source = "C:\Repo Prueba\Fshop"
destination = "C:\Repo Prueba\Fshop\Reportes"
archivos_csv = [archivo for archivo in os.listdir(source) if archivo.endswith('.csv')]
for archivo_csv in archivos_csv:
    if fecha_actual in archivo_csv:
        ruta_archivo = os.path.join(source, archivo_csv)
        shutil.move(ruta_archivo, destination)