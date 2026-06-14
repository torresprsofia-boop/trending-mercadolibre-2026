import requests
import pandas as pd
import os

# CONFIGURACION - usa variable de entorno o reemplaza con tu token
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "TU_TOKEN_AQUI")
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

print("Consultando API de Mercado Libre...")

r = requests.get("https://api.mercadolibre.com/trends/MLA", headers=headers)
trends = r.json()

def categorizar(keyword):
    keyword = keyword.lower()
    if any(x in keyword for x in ["iphone", "samsung", "celular", "nokia", "motorola", "moto"]):
        return "Celulares"
    elif any(x in keyword for x in ["aire", "lavarropas", "heladera", "microondas", "cafetera", "pava", "termotanque"]):
        return "Electrodomesticos"
    elif any(x in keyword for x in ["notebook", "dell", "chromecast", "proyector", "auricular"]):
        return "Tecnologia"
    elif any(x in keyword for x in ["zapatillas", "botines", "vans", "nike", "adidas"]):
        return "Calzado"
    elif any(x in keyword for x in ["playstation", "play 5", "ps5"]):
        return "Videojuegos"
    else:
        return "Otros"

registros = [{"posicion": i+1, "keyword": t["keyword"], "categoria": categorizar(t["keyword"])} for i, t in enumerate(trends)]
df = pd.DataFrame(registros)

print(f"Se encontraron {len(df)} productos trending")
print(df)

df.to_csv("trends_mercadolibre.csv", index=False)
print("CSV guardado!")
