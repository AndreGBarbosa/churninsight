from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# 1. Carregar o Pipeline (que já contém Scaler + Modelo)
try:
    # Tenta carregar o arquivo oficial
    model_pipeline = joblib.load('pipeline_churn_hackathon.joblib')
    print(">>> SUCESSO: Pipeline oficial carregado!")
except Exception as e:
    print(f">>> AVISO: Não achei o pipeline oficial ({e}).")
    print(">>> Tentando carregar modelo MVP local para não parar o servidor...")
    try:
        model_pipeline = joblib.load('modelo_mvp_13_features.joblib')
    except:
        print(">>> ERRO CRÍTICO: Nenhum modelo encontrado.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # 2. Definir as colunas EXATAS que o modelo espera (Ordem importa!)
        features_esperadas = [
            'months', 'rev_Mean', 'mou_Mean', 'totcalls', 'eqpdays',
            'rev_per_minute', 'calls_per_month', 'eqp_age_index',
            'custcare_Mean', 'drop_vce_Mean', 'blck_vce_Mean', 'avgmou', 'avgrev'
        ]
        
        # 3. Criar DataFrame garantindo a ordem das colunas
        # Se o Java não mandar algum campo, preenchemos com 0 para não travar
        df_input = pd.DataFrame([data])
        
        # Garante que todas as colunas existem (preenche com 0 se faltar)
        for col in features_esperadas:
            if col not in df_input.columns:
                df_input[col] = 0
                
        # Seleciona apenas as colunas certas na ordem certa
        df_final = df_input[features_esperadas]
        
        # 4. Previsão (O pipeline já faz o Scalling sozinho!)
        prediction = model_pipeline.predict(df_final)[0]
        probability = model_pipeline.predict_proba(df_final)[0][1]

        return jsonify({
            "previsao": "Vai cancelar" if prediction == 1 else "Vai continuar",
            "probabilidade": round(float(probability), 2)
        })

    except Exception as e:
        return jsonify({"erro": f"Erro no processamento: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')