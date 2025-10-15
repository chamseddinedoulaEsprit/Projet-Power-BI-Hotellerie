# 🏨 Projet Power BI : Analyse des Réservations Hôtelières

## 📋 Description du Projet

Ce projet consiste en une analyse complète des données de réservations hôtelières pour les années 2023 et 2024, avec création de tableaux de bord interactifs Power BI. L'objectif est d'extraire des insights stratégiques pour optimiser les performances hôtelières, améliorer l'expérience client et maximiser les revenus.

## 🎯 Objectifs

- **Analyser les tendances** de réservations sur 2023-2024
- **Identifier les facteurs** influençant les annulations
- **Optimiser la gestion** des chambres et services
- **Évaluer la satisfaction** client et la fidélisation
- **Créer des visualisations** interactives pour la prise de décision

## 📊 Structure du Projet

```
Projet-Power-BI-Hotellerie/
│
├── hotel_reservations_2023.xlsx          # Données brutes 2023
├── hotel_reservations_2024.xlsx          # Données brutes 2024
├── hotel_reservations_clean_merged.csv   # Dataset nettoyé et fusionné
├── hotel_reservations_data_dictionary.csv # Dictionnaire des données
├── hotel_reservations_data_understanding.ipynb # Notebook d'exploration
└── README.md                             # Documentation du projet
```

## 📁 Description des Fichiers

### 1. **hotel_reservations_data_dictionary.csv**
Dictionnaire de données détaillant toutes les colonnes du dataset :
- **Guest ID** : Identifiant unique du client
- **Reservation ID** : Identifiant unique de la réservation
- **Check-In/Out Date** : Dates d'arrivée et de départ
- **Room Type** : Type de chambre (Single, Double, Suite)
- **Booking Channel** : Canal de réservation (Online, Direct, Corporate)
- **Payment Method** : Mode de paiement
- **Total Amount** : Montant total en USD
- **Cancellation Status** : Statut d'annulation
- **Guest Rating** : Note client (1-5)
- Et bien d'autres...

### 2. **hotel_reservations_data_understanding.ipynb**
Notebook Jupyter Python contenant :
- ✅ Fusion des datasets 2023 et 2024
- ✅ Analyse exploratoire complète (EDA)
- ✅ Détection et traitement des valeurs manquantes
- ✅ Identification des outliers
- ✅ Analyse PCA et clustering
- ✅ Modèle RandomForest pour prédire les annulations
- ✅ Visualisations avec interprétations

### 3. **hotel_reservations_clean_merged.csv**
Dataset final nettoyé et prêt pour Power BI, contenant :
- Données fusionnées 2023-2024
- Valeurs manquantes traitées
- Colonne `year` ajoutée pour analyses temporelles

## 🔍 Analyses Réalisées

### 📈 Analyses Descriptives
- Distribution des réservations par canal de vente
- Analyse des types de chambres réservées
- Tendances saisonnières et temporelles
- Répartition géographique des clients

### 💰 Analyses Financières
- Revenus totaux par période
- Prix moyen par type de chambre
- Coûts des services supplémentaires
- Impact des annulations sur le chiffre d'affaires

### 👥 Analyses Client
- Segmentation de la clientèle
- Fréquence des visites (First-time, Regular, VIP)
- Programme de fidélité (Gold, Silver, Bronze)
- Satisfaction client (ratings et reviews)

### ⚠️ Analyses Prédictives
- Facteurs de risque d'annulation
- Importance des features (RandomForest)
- Clustering des profils clients
- Analyse en composantes principales (PCA)

## 🛠️ Technologies Utilisées

- **Power BI** : Visualisation et tableaux de bord
- **Python 3.x** : Traitement et analyse des données
  - pandas : Manipulation de données
  - numpy : Calculs numériques
  - matplotlib & seaborn : Visualisations
  - scikit-learn : Machine Learning
  - openpyxl : Lecture Excel
- **Jupyter Notebook** : Environnement d'exploration

## 🚀 Guide d'Utilisation

### Prérequis
```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl jupyter
```

### Étapes d'Exécution

1. **Exploration des données**
   ```bash
   jupyter notebook hotel_reservations_data_understanding.ipynb
   ```
   Exécutez toutes les cellules pour générer le fichier nettoyé.

2. **Import dans Power BI**
   - Ouvrir Power BI Desktop
   - Importer `hotel_reservations_clean_merged.csv`
   - Utiliser le dictionnaire de données comme référence
   - Créer les relations et mesures DAX nécessaires

3. **Création des visualisations**
   - Tableaux de bord des KPIs
   - Analyses des tendances temporelles
   - Segmentation client
   - Rapports d'annulation

## 📊 KPIs Clés à Suivre

- **Taux d'occupation** : Nombre de chambres réservées / Total chambres
- **ADR (Average Daily Rate)** : Revenu moyen par chambre par jour
- **RevPAR (Revenue Per Available Room)** : Revenu par chambre disponible
- **Taux d'annulation** : Annulations / Total réservations
- **Lead Time moyen** : Délai moyen entre réservation et check-in
- **Score de satisfaction** : Note moyenne des clients
- **Taux de fidélisation** : Clients réguliers / Total clients

## 📌 Insights Potentiels

- Identification des périodes de forte/faible demande
- Canaux de réservation les plus rentables
- Profils clients à fort potentiel
- Motifs d'annulation récurrents
- Services supplémentaires les plus demandés
- Impact du programme de fidélité

## 👨‍💻 Auteur

**Chamseddine Doula**
- GitHub: [@chamseddinedoulaEsprit](https://github.com/chamseddinedoulaEsprit)
- Projet: Power BI Hôtellerie

## 📝 Licence

Ce projet est réalisé dans le cadre d'un projet académique (PIDEV).

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouvelles analyses

## 📞 Contact

Pour toute question ou suggestion concernant ce projet, n'hésitez pas à me contacter.

---

**Note** : Assurez-vous d'avoir les fichiers Excel `hotel_reservations_2023.xlsx` et `hotel_reservations_2024.xlsx` dans le répertoire avant d'exécuter le notebook.
