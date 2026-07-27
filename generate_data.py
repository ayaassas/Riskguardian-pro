import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 5000

print("⏳ Génération des données de surveillance AML (Anti-Money Laundering)...")

# 1. Profil du compte
age_compte_mois = np.random.randint(1, 120, size=n_samples)
volume_moyen_mensuel = np.random.exponential(scale=5000, size=n_samples).clip(500, 100000)

# 2. Indicateurs AML (Typologies officielles)
ratio_depots_cash = np.random.beta(1, 5, size=n_samples) * 100
nombre_transactions_sous_seuil = np.random.poisson(lam=1.2, size=n_samples).clip(0, 15)
virements_pays_risque_30j = np.random.choice([0, 1, 2, 3, 5], size=n_samples, p=[0.80, 0.12, 0.05, 0.02, 0.01])
temps_conservation_fonds_heures = np.random.exponential(scale=48, size=n_samples).clip(0.5, 720)

# 3. Calcul de suspicion (Score AML)
score_latent = (
    (ratio_depots_cash * 0.04)
    + (nombre_transactions_sous_seuil * 0.35)
    + (virements_pays_risque_30j * 1.1)
    - (np.log1p(temps_conservation_fonds_heures) * 0.4)
    - (np.log1p(age_compte_mois) * 0.15)
)

probabilite_suspicion = 1 / (1 + np.exp(-(score_latent - 2.0)))
est_suspect = (probabilite_suspicion > np.random.uniform(0, 1, size=n_samples)).astype(int)

# 4. Enregistrement dans le tableau
df = pd.DataFrame(
    {
        "id_compte": [f"ACC-{20000 + i}" for i in range(n_samples)],
        "age_compte_mois": age_compte_mois,
        "volume_mensuel_eur": np.round(volume_moyen_mensuel, 2),
        "ratio_depots_cash": np.round(ratio_depots_cash, 2),
        "transactions_sous_seuil_10k": nombre_transactions_sous_seuil,
        "virements_pays_risque_30j": virements_pays_risque_30j,
        "temps_conservation_fonds_h": np.round(temps_conservation_fonds_heures, 1),
        "alerte_blanchiment": est_suspect,
    }
)

df.to_csv("donnees_banque.csv", index=False)
print(f"✅ Fichier 'donnees_banque.csv' généré avec succès ({n_samples} comptes analysés) !")