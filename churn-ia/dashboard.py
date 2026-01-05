import streamlit as st
import requests

st.set_page_config(page_title="ChurnInsight", page_icon="📊")

st.title("📊 ChurnInsight - Análise de Risco")
st.write("Preencha os dados abaixo para verificar a probabilidade de cancelamento.")

# Formulário para os 13 campos
with st.form("churn_form"):
    st.subheader("1. Dados do Contrato")
    col1, col2 = st.columns(2)
    with col1:
        months = st.number_input("Tempo de Contrato (meses)", min_value=1, value=12)
        rev_mean = st.number_input("Fatura Média (R$)", min_value=0.0, value=55.5)
        avgrev = st.number_input("Média Histórica Receita (R$)", min_value=0.0, value=50.0)
    with col2:
        totcalls = st.number_input("Total de Chamadas", min_value=0, value=45)
        eqpdays = st.number_input("Idade do Equipamento (dias)", min_value=0, value=300)
        eqp_age_index = st.number_input("Índice Idade Equipamento", min_value=0.0, value=1.5)

    st.subheader("2. Uso e Comportamento")
    col3, col4 = st.columns(2)
    with col3:
        mou_mean = st.number_input("Minutos de Uso (Média)", min_value=0.0, value=200.0)
        avgmou = st.number_input("Média Histórica Minutos", min_value=0.0, value=190.0)
        rev_per_minute = st.number_input("Custo por Minuto", min_value=0.0, value=0.27)
    with col4:
        calls_per_month = st.number_input("Chamadas por Mês", min_value=0.0, value=3.75)
        custcare_Mean = st.number_input("Chamadas para Suporte", min_value=0.0, value=2.0)

    st.subheader("3. Qualidade da Chamada")
    col5, col6 = st.columns(2)
    with col5:
        drop_vce_Mean = st.number_input("Chamadas Caídas", min_value=0.0, value=1.0)
    with col6:
        blck_vce_Mean = st.number_input("Chamadas Bloqueadas", min_value=0.0, value=0.5)
    
    submit = st.form_submit_button("🔍 Analisar Cliente", type="primary")

if submit:
    # Monta o JSON com as 13 colunas
    payload = {
        "months": months,
        "rev_Mean": rev_mean,
        "mou_Mean": mou_mean,
        "totcalls": totcalls,
        "eqpdays": eqpdays,
        "rev_per_minute": rev_per_minute,
        "calls_per_month": calls_per_month,
        "eqp_age_index": eqp_age_index,
        "custcare_Mean": custcare_Mean,
        "drop_vce_Mean": drop_vce_Mean,
        "blck_vce_Mean": blck_vce_Mean,
        "avgmou": avgmou,
        "avgrev": avgrev
    }
    
    try:
        # Chama a API Java
        response = requests.post("http://localhost:8080/api/churn/analise", json=payload)
        
        if response.status_code == 200:
            resultado = response.json()
            previsao = resultado['previsao']
            prob = resultado['probabilidade'] * 100
            
            st.divider()
            if previsao == "Vai cancelar":
                st.error(f"🚨 **ALERTA DE CHURN DETECTADO!**")
                st.metric(label="Probabilidade de Saída", value=f"{prob:.1f}%", delta="-Alto Risco")
            else:
                st.success(f"✅ **CLIENTE SEGURO**")
                st.metric(label="Probabilidade de Saída", value=f"{prob:.1f}%", delta="Baixo Risco")
        else:
            st.error(f"Erro na API Java: {response.status_code}")
            
    except Exception as e:
        st.error(f"Erro de conexão: Verifique se o Java está rodando. ({e})")