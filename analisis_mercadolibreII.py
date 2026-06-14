import requests
import pandas as pd
import matplotlib.pyplot as plt

ACCESS_TOKEN = "APP_USR-8024101437347323-061314-ccb6b820438b91d705424595fa248f9f-1304833505"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

print("🔍 Consultando trends de Mercado Libre...")

r = requests.get("https://api.mercadolibre.com/trends/MLA", headers=headers)
trends = r.json()

# Categorizar productos
def categorizar(keyword):
    keyword = keyword.lower()
    if any(x in keyword for x in ["iphone", "samsung", "celular", "nokia", "motorola", "moto"]):
        return "Celulares"
    elif any(x in keyword for x in ["aire", "lavarropas", "heladera", "microondas", "cafetera", "pava", "termotanque"]):
        return "Electrodomésticos"
    elif any(x in keyword for x in ["notebook", "dell", "chromecast", "proyector", "auricular"]):
        return "Tecnología"
    elif any(x in keyword for x in ["zapatillas", "botines", "vans", "nike", "adidas"]):
        return "Calzado"
    elif any(x in keyword for x in ["playstation", "play 5", "ps5"]):
        return "Videojuegos"
    elif any(x in keyword for x in ["reloj", "termo", "cortina"]):
        return "Hogar y Accesorios"
    else:
        return "Otros"

registros = []
for i, t in enumerate(trends):
    registros.append({
        "posicion": i + 1,
        "keyword": t["keyword"],
        "categoria": categorizar(t["keyword"]),
        "url": t["url"]
    })

df = pd.DataFrame(registros)

print(f"✅ {len(df)} productos trending")
print(df[["posicion", "keyword", "categoria"]].to_string())

# Exportar CSV
df.to_csv("trends_mercadolibre.csv", index=False)
print("\n💾 CSV guardado: trends_mercadolibre.csv")

# Graficos
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Productos Trending - Mercado Libre Argentina", fontsize=14)

# Grafico 1: Cantidad por categoría
cat_counts = df["categoria"].value_counts()
axes[0].bar(cat_counts.index, cat_counts.values, 
            color=["#3498db","#2ecc71","#e74c3c","#f39c12","#9b59b6","#1abc9c","#e67e22"])
axes[0].set_title("Trending por categoría")
axes[0].set_ylabel("Cantidad")
axes[0].tick_params(axis='x', rotation=45)

# Grafico 2: Pie chart
axes[1].pie(cat_counts.values, labels=cat_counts.index, autopct="%1.1f%%")
axes[1].set_title("Distribución de categorías")

plt.tight_layout()
plt.savefig("grafico_trends.png", dpi=150)
plt.show()
print("✅ Gráfico guardado!")
