# 📊 Trending Mercado Libre Argentina · 13/06/2026

Análisis de los 50 productos más buscados en Mercado Libre Argentina en tiempo real, utilizando la API REST oficial con autenticación OAuth 2.0.

## 🔍 ¿Qué hace este proyecto?

Conecta Python al endpoint `/trends/MLA` de la API de Mercado Libre, extrae los 50 productos trending del día, los clasifica por categoría y exporta el dataset a CSV para su visualización en Tableau Public.

## 🚀 Resultado

Entre celulares, electrodomésticos, tecnología, calzado y videojuegos... el producto #1 del trending en Argentina no pertenece a ninguna de esas categorías.

**Es el álbum de figuritas Panini del Mundial 2026.** 🏆⚽

## 🛠️ Stack

- Python 3.14
- requests
- pandas
- OAuth 2.0
- REST API
- JSON
- Tableau Public
- VS Code

## 📁 Archivos

| Archivo | Descripción |
|---------|-------------|
| `analisis_mercadolibre.py` | Script principal de extracción y análisis |
| `trends_mercadolibre.csv` | Dataset exportado con los 50 productos trending |

## ⚙️ Cómo ejecutarlo

1. Cloná el repositorio
```bash
git clone https://github.com/torresprsofia-boop/trending-mercadolibre-2026
```

2. Instalá las dependencias
```bash
pip install requests pandas matplotlib
```

3. Ejecutá el script
```bash
python analisis_mercadolibre.py
```

## 📊 Dashboard

Visualización interactiva disponible en Tableau Public.

## 👩‍💻 Autora

Sofia Torres — Analista de Datos
