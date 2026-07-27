import pandas as pd
import xgboost as xgb
import shap
import pickle

print("⏳ Entraînement de l'IA XGBoost pour la surveillance AML...")

# 1. Chargement des données bancaires générées
df = pd.read_csv("donnees_banque.csv")
X = df.drop(columns=["id_compte", "alerte_blanchiment"])
y = df["alerte_blanchiment"]

# 2. Entraînement du modèle XGBoost
model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.05,
    scale_pos_weight=3,
    random_state=42
)
model.fit(X, y)

# 3. Moteur d'explicabilité SHAP
explainer = shap.TreeExplainer(model)

# 4. Sauvegarde dans aml_model.pkl
with open("aml_model.pkl", "wb") as f:
    pickle.dump({"model": model, "feature_names": list(X.columns), "explainer": explainer}, f)

print("✅ Modèle XGBoost entraîné avec succès !")
print("✅ Le fichier 'aml_model.pkl' a bien été créé !")