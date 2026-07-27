# RiskGuardian Pro
> Plateforme décisionnelle MLOps & Explicabilité pour la conformité LCB-FT / AML

RiskGuardian Pro est une solution logicielle conçue pour assister les analystes conformité dans la détection du blanchiment d'argent et du financement du terrorisme. L'application combine une architecture de prédiction sous XGBoost, une explicabilité locale et globale via SHAP, ainsi qu'une persistance des données sous SQLite pour garantir la traçabilité des audits.

---

### Liens utiles
* **Démonstration interactive (Streamlit) :** https://riskguardian-pro.streamlit.app
* **Dépôt du code source (GitHub) :** https://github.com/votre-nom/riskguardian-pro

---

## Architecture & Fonctionnalités

| Module | Description technique |
| :--- | :--- |
| **Audit Transactionnel** | Simulation temps réel de profils financiers (comptes normaux, schémas de smurfing, comptes de transit) et calcul du score de risque. |
| **Explicabilité (XGBoost + SHAP)** | Décomposition de la contribution de chaque variable (dépôts d'espèces, opérations sous le seuil légal, ratios de rétention) au score global. |
| **Suivi de Performance (MLOps)** | Évaluation du modèle via matrice de confusion, métriques ROC-AUC (0.96) et importance des variables. |
| **Registre & Traçabilité SQL** | Archivage local des décisions d'audit dans une base de données SQLite pour contrôle de conformité. |

---

## Technologies Utilisées

* **Core & Processing :** Python 3.10+, Pandas, NumPy
* **Modélisation & Interprétabilité :** XGBoost, SHAP, Scikit-Learn
* **Interface & Déploiement :** Streamlit, Streamlit Community Cloud
* **Base de données :** SQLite3

---

## Installation et Exécution Locale

```bash
# Clone du dépôt
git clone [https://github.com/votre-nom/riskguardian-pro.git](https://github.com/votre-nom/riskguardian-pro.git)
cd riskguardian-pro

# Installation des dépendances
pip install -r requirements.txt

# Lancement de l'application
python -m streamlit run app.py
