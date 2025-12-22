from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar o Modelo e o Scaler MVP (que criamos no passo anterior)
# Usamos try/except para evitar travar se o arquivo nao existir
try:
    modelo = joblib.load('modelo_mvp.joblib')
    scaler = joblib.load('scaler_mvp.joblib')
    print(">>> SUCESSO: Modelo MVP carregado!")
except Exception as e:
    print(f">>> ERRO CRÍTICO: Não achei os arquivos .joblib. Detalhe: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        df_input = pd.DataFrame([data])
        
        # O Scaler espera os dados na mesma ordem do treinamento
        dados_escalados = scaler.transform(df_input)
        
        prediction = modelo.predict(dados_escalados)[0]
        probability = modelo.predict_proba(dados_escalados)[0][1]

        return jsonify({
            "previsao": "Vai cancelar" if prediction == 1 else "Vai continuar",
            "probabilidade": round(float(probability), 2)
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')