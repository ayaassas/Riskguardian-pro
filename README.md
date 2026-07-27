# RiskGuardian Pro
> Plateforme décisionnelle MLOps et Explicabilité pour la conformité LCB-FT et AML

RiskGuardian Pro est une solution logicielle conçue pour assister les analystes conformité dans la détection du blanchiment d'argent. L'application combine une architecture de prédiction sous XGBoost, une explicabilité locale et globale via SHAP, ainsi qu'une persistance des données sous SQLite pour garantir la traçabilité des audits.

---

### Liens d'accès

| Ressource | Lien direct |
| :--- | :--- |
| **Démonstration interactive** | [Ouvrir l'application Streamlit](https://riskguardian-pro-cnbntyjnydvruzjhv2atdc.streamlit.app/) |
| **Code source du projet** | [Consulter le dépôt GitHub](https://github.com/ayaassas/riskguardian-pro) |

---

## Architecture et Modules Métier

<table width="100%">
  <thead>
    <tr>
      <th align="left" width="30%">Module</th>
      <th align="left" width="70%">Description fonctionnelle et technique</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Audit Transactionnel</b></td>
      <td>Simulation en temps réel de profils financiers (comptes normaux, schémas de smurfing, comptes de transit) et évaluation instantanée du score de risque.</td>
    </tr>
    <tr>
      <td><b>Explicabilité IA (XGBoost et SHAP)</b></td>
      <td>Décomposition fine de la contribution de chaque variable (dépôts d'espèces, opérations sous le seuil légal, ratios de rétention) au calcul du risque.</td>
    </tr>
    <tr>
      <td><b>Suivi de Performance (MLOps)</b></td>
      <td>Supervision de la qualité du modèle via matrice de confusion, métriques ROC-AUC et classement de l'importance des variables.</td>
    </tr>
    <tr>
      <td><b>Registre et Traçabilité SQL</b></td>
      <td>Archivage et historique des décisions d'audit dans une base de données SQLite pour contrôle de conformité.</td>
    </tr>
  </tbody>
</table>

---

## Stack Technique

* **Traitement et Analyse :** Python 3.10+, Pandas, NumPy
* **Modélisation et Interprétabilité :** XGBoost, SHAP, Scikit-Learn
* **Interface et Déploiement :** Streamlit, Streamlit Community Cloud
* **Base de données :** SQLite3

---

## Installation et Exécution Locale

```bash
# Clonage du dépôt
git clone [https://github.com/ayaassas/riskguardian-pro.git](https://github.com/ayaassas/riskguardian-pro.git)
cd riskguardian-pro

# Installation des dépendances
pip install -r requirements.txt

# Lancement de l'application
python -m streamlit run app.py
