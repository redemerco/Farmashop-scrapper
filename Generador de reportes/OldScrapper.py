import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
url = "https://tienda.farmashop.com.uy/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
start = time.time()
#find product link
productUrl=list()
mainUrls=list()
sku=list()
name=list()
price=list()

#scrap navigation urls
for i in soup.find_all("a", class_="nav-anchor", href=True):
    mainUrls.append(i['href'].replace("#","https://tienda.farmashop.com.uy/"))
mainUrls =list(dict.fromkeys(mainUrls))

for i in mainUrls:
    r = requests.get(i)
    soup = BeautifulSoup(r.content, "html.parser")
    for i in soup.find_all('a', class_="product-item-link", href=True):
        productUrl.append(i['href'])
    for i in productUrl:
        r = requests.get(i)
        soup = BeautifulSoup(r.content, "html.parser")
        textSku=soup.find('div', class_="product attribute sku")
        sku.append(textSku.get_text().replace("\nSKU\n","").replace("\n",""))
        textName=soup.find('span', class_="base")
        name.append(textName.get_text().replace("\xa0",""))
        textPrice=soup.find('span', class_="price-wrapper")
        price.append(textPrice.get_text().replace("\xa0", "" ))
    data=(name,price,sku)
    df= pd.DataFrame(data)
    realdf= df.transpose()
    realdf.to_csv('reporte.csv', index=False)
    productUrl.clear()
end=time.time()
print(((end - start)/60)/60, "hrs")