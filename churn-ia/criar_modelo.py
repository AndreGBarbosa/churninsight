import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

print("Criando Pipeline Mock com 13 features...")

# 1. Colunas exigidas
features = [
    'months', 'rev_Mean', 'mou_Mean', 'totcalls', 'eqpdays',
    'rev_per_minute', 'calls_per_month', 'eqp_age_index',
    'custcare_Mean', 'drop_vce_Mean', 'blck_vce_Mean', 'avgmou', 'avgrev'
]

# 2. Dados falsos para treino (100 linhas)
df = pd.DataFrame(np.random.randint(0, 100, size=(100, len(features))), columns=features)
y = np.random.randint(0, 2, size=100)

# 3. Criar Pipeline (Scaler + Modelo juntos)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=10))
])

pipeline.fit(df, y)

# 4. Salvar
joblib.dump(pipeline, 'modelo_mvp_13_features.joblib')
print("✅ Arquivo 'modelo_mvp_13_features.joblib' criado com sucesso.")