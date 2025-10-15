import pandas as pd

# -----------------------------
# 1. Charger les données
# -----------------------------
df_2023 = pd.read_excel("hotel_reservations_2023.xlsx")
df_2024 = pd.read_excel("hotel_reservations_2024.xlsx")
data_dict = pd.read_csv("hotel_reservations_data_dictionary.csv")

print("✅ Données chargées :")
print(f"- 2023 : {df_2023.shape}")
print(f"- 2024 : {df_2024.shape}")
print(f"- Dictionnaire : {data_dict.shape}")

# -----------------------------
# 2. Fusionner les datasets
# -----------------------------
df_all = pd.concat([df_2023, df_2024], ignore_index=True)

print("\n✅ Données fusionnées :")
print(df_all.shape)

# -----------------------------
# 3. Vérification colonnes selon dictionnaire
# -----------------------------
colonnes_dict = data_dict["Column Name"].tolist()
df_all = df_all[[c for c in df_all.columns if c in colonnes_dict]]

# -----------------------------
# 4. Nettoyage des données
# -----------------------------
# Exemple : remplacer les valeurs manquantes
df_all = df_all.fillna({
    "children": 0,
    "babies": 0
})

# Convertir certaines colonnes en bonnes catégories
if "arrival_date" in df_all.columns:
    df_all["arrival_date"] = pd.to_datetime(df_all["arrival_date"], errors="coerce")

# -----------------------------
# 5. KPI de base
# -----------------------------
print("\n📊 Indicateurs clés :")
print(f"- Nombre total de réservations : {len(df_all)}")
print(f"- Taux d'annulation : {df_all['is_canceled'].mean():.2%}" if "is_canceled" in df_all.columns else "Pas de colonne annulation")
print(f"- Durée moyenne des séjours : {df_all['stays_in_weekend_nights'].mean() + df_all['stays_in_week_nights'].mean():.1f} nuits")

# -----------------------------
# 6. Export pour BI
# -----------------------------
df_all.to_csv("hotel_reservations_clean.csv", index=False)
df_all.to_parquet("hotel_reservations_clean.parquet", index=False)

print("\n✅ Données prêtes pour Power BI / Tableau : 'hotel_reservations_clean.csv'")
