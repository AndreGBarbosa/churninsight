import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

print("Criando modelo MVP compatível com suas 5 colunas...")

# 1. Simular dados de treinamento (já que não temos o CSV original fácil)
# Criamos 1000 clientes falsos com as 5 colunas que seu Java manda
dados = {
    'months': np.random.randint(1, 72, 1000),      # 1 a 72 meses
    'rev_Mean': np.random.uniform(20, 200, 1000),  # Conta de 20 a 200 reais
    'mou_Mean': np.random.uniform(10, 1000, 1000), # Minutos de uso
    'totcalls': np.random.randint(0, 500, 1000),   # Total de chamadas
    'eqpdays': np.random.randint(0, 1000, 1000),   # Idade do equipamento
    'churn': np.random.randint(0, 2, 1000)         # 0 ou 1 (Cancelou ou não)
}

df = pd.DataFrame(dados)

# Separar entrada (X) e saída (y)
X = df[['months', 'rev_Mean', 'mou_Mean', 'totcalls', 'eqpdays']]
y = df['churn']

# 2. Criar e treinar o Scaler (A régua)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Criar e treinar o Modelo (O cérebro)
modelo = RandomForestClassifier(n_estimators=50, random_state=42)
modelo.fit(X_scaled, y)

# 4. Salvar os arquivos novos
joblib.dump(modelo, 'modelo_mvp.joblib')
joblib.dump(scaler, 'scaler_mvp.joblib')

print("✅ SUCESSO! Arquivos 'modelo_mvp.joblib' e 'scaler_mvp.joblib' criados.")