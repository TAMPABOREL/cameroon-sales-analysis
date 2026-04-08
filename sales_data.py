# ================================================
# Cameroon Sales & Revenue Analysis
# Generating the dataset
# ================================================

import pandas as pd
import numpy as np

# Setting seed for reproducibility
np.random.seed(42)

# Number of records
n = 1000

# Cameroonian cities
cities = ['Douala', 'Yaoundé', 'Bafoussam', 'Garoua', 'Bamenda', 'Maroua']

# Product categories
categories = ['Électronique', 'Alimentation', 'Vêtements', 'Mobilier', 'Cosmétiques']

# Products per category
products = {
    'Électronique' : ['Téléphone', 'Ordinateur', 'Télévision', 'Tablette'],
    'Alimentation' : ['Riz', 'Huile', 'Farine', 'Sucre'],
    'Vêtements'    : ['Chemise', 'Pantalon', 'Robe', 'Chaussures'],
    'Mobilier'     : ['Canapé', 'Table', 'Chaise', 'Armoire'],
    'Cosmétiques'  : ['Crème', 'Parfum', 'Shampoing', 'Savon'],
}

# Customer segments
segments = ['Particulier', 'PME', 'Grande Entreprise']

# Sales channels
channels = ['Boutique', 'En ligne', 'Grossiste']

# ── GENERATING RECORDS ──────────────────────────
# Generating random categories
random_categories = np.random.choice(list(products.keys()), n)

# Generating matching products based on category
random_products = [
    np.random.choice(products[cat]) 
    for cat in random_categories
]

# Generating dates between 2023 and 2024
dates = pd.date_range(
    start='2023-01-01', 
    end='2024-12-31', 
    periods=n
).to_series().sample(frac=1).reset_index(drop=True)

# Building the dataset
data = {
    'date'            : dates,
    'city'            : np.random.choice(cities, n),
    'category'        : random_categories,
    'product'         : random_products,
    'segment'         : np.random.choice(segments, n),
    'channel'         : np.random.choice(channels, n),
    'quantity'        : np.random.randint(1, 50, n),
    'unit_price_fcfa' : np.random.randint(1000, 500000, n),
    'discount_pct'    : np.random.choice([0, 5, 10, 15, 20], n),
}

# Creating DataFrame
df = pd.DataFrame(data)

# Calculating revenue
df['revenue_fcfa'] = (
    df['quantity'] * df['unit_price_fcfa'] * 
    (1 - df['discount_pct'] / 100)
).astype(int)

# Extracting date parts for Power BI
df['year']  = df['date'].dt.year
df['month'] = df['date'].dt.month
df['month_name'] = df['date'].dt.strftime('%B')

# Displaying summary
print("=" * 50)
print("  CAMEROON SALES DATASET - SUMMARY")
print("=" * 50)
print(f"Total records    : {len(df):,}")
print(f"Total revenue    : {df['revenue_fcfa'].sum():,} FCFA")
print(f"Average revenue  : {df['revenue_fcfa'].mean():,.0f} FCFA")
print(f"Date range       : 2023 - 2024")
print(f"Cities           : {', '.join(cities)}")

# ── EXPORTING TO EXCEL ──────────────────────────
# Installing openpyxl first if needed
# pip install openpyxl

# Saving to Excel
df.to_excel('cameroon_sales_data.xlsx', index=False)

print("\n✅ Dataset saved → cameroon_sales_data.xlsx")
print(f"Rows    : {len(df):,}")
print(f"Columns : {len(df.columns)}")
print("\nColumns list:")
for col in df.columns:
    print(f"  • {col}")
