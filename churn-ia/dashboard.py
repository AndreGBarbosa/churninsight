import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="ChurnInsight", page_icon="📊", layout="wide")

# Estilo profissional (dark mode customizado)
st.markdown("""
    <style>
        .stApp { background-color: #0f172a; color: white; }
        input, textarea { background-color: #1e293b !important; color: white !important; }
        .stButton>button { background-color: #22c55e; color: black; font-weight: bold; border-radius: 5px; }
        .positive { color: #22c55e; font-weight: bold; }
        .negative { color: #ef4444; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho verde neon
st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #22c55e, #16a34a, #065f46);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0px 0px 20px #22c55e;
    ">
        <h1 style="color: #bbf7d0; margin: 0; font-size: 42px; font-weight: bold; text-shadow: 0px 0px 10px #22c55e;">
            🔍 ChurnInsight
        </h1>
        <h3 style="color: #86efac; margin-top: 10px; font-size: 22px; font-weight: normal; text-shadow: 0px 0px 8px #22c55e;">
            Análise de Risco de Cancelamento
        </h3>
        <p style="color: #d1fae5; font-size: 16px; margin-top: 5px;">
            Preencha os dados abaixo e descubra a probabilidade de saída do cliente.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Formulário com layout em colunas
with st.form("churn_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        months = st.number_input("Tempo de Contrato (meses)", min_value=1, value=12)
        st.markdown("<span class='positive'>Contrato longo</span>" if months >= 6 else "<span class='negative'>Contrato curto</span>", unsafe_allow_html=True)

        rev_mean = st.number_input("Fatura Média (R$)", min_value=0.0, value=55.5)
        st.markdown("<span class='positive'>Fatura saudável</span>" if rev_mean >= 30 else "<span class='negative'>Fatura baixa</span>", unsafe_allow_html=True)

        avgrev = st.number_input("Média Histórica Receita (R$)", min_value=0.0, value=50.0)
        st.markdown("<span class='positive'>Receita consistente</span>" if avgrev >= 30 else "<span class='negative'>Receita baixa</span>", unsafe_allow_html=True)

        eqp_age_index = st.number_input("Índice Idade Equipamento", min_value=0.0, value=1.5)
        st.markdown("<span class='positive'>Equipamento em bom estado</span>" if eqp_age_index < 3 else "<span class='negative'>Equipamento obsoleto</span>", unsafe_allow_html=True)

    with col2:
        mou_mean = st.number_input("Minutos de Uso (Média)", min_value=0.0, value=200.0)
        st.markdown("<span class='positive'>Uso consistente</span>" if mou_mean >= 100 else "<span class='negative'>Pouco uso</span>", unsafe_allow_html=True)

        avgmou = st.number_input("Média Histórica Minutos", min_value=0.0, value=190.0)
        st.markdown("<span class='positive'>Histórico de uso bom</span>" if avgmou >= 100 else "<span class='negative'>Histórico de uso baixo</span>", unsafe_allow_html=True)

        rev_per_minute = st.number_input("Custo por Minuto", min_value=0.0, value=0.27)
        st.markdown("<span class='positive'>Custo competitivo</span>" if rev_per_minute <= 0.5 else "<span class='negative'>Custo elevado</span>", unsafe_allow_html=True)

        calls_per_month = st.number_input("Chamadas por Mês", min_value=0.0, value=3.75)
        st.markdown("<span class='positive'>Uso regular</span>" if calls_per_month >= 3 else "<span class='negative'>Poucas chamadas</span>", unsafe_allow_html=True)

    with col3:
        totcalls = st.number_input("Total de Chamadas", min_value=0, value=45)
        st.markdown("<span class='positive'>Cliente ativo</span>" if totcalls >= 20 else "<span class='negative'>Cliente pouco ativo</span>", unsafe_allow_html=True)

        eqpdays = st.number_input("Idade do Equipamento (dias)", min_value=0, value=300)
        st.markdown("<span class='positive'>Equipamento relativamente novo</span>" if eqpdays < 1000 else "<span class='negative'>Equipamento muito antigo</span>", unsafe_allow_html=True)

        custcare_Mean = st.number_input("Chamadas para Suporte", min_value=0.0, value=2.0)
        st.markdown("<span class='positive'>Poucas chamadas de suporte</span>" if custcare_Mean <= 5 else "<span class='negative'>Muitas chamadas de suporte</span>", unsafe_allow_html=True)

        drop_vce_Mean = st.number_input("Chamadas Caídas", min_value=0.0, value=1.0)
        blck_vce_Mean = st.number_input("Chamadas Bloqueadas", min_value=0.0, value=0.5)
        if drop_vce_Mean > 3 or blck_vce_Mean > 3:
            st.markdown("<span class='negative'>Problemas frequentes de chamadas</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span class='positive'>Qualidade de chamadas estável</span>", unsafe_allow_html=True)

    submit = st.form_submit_button("🔍 Analisar Cliente")

# Processamento da API
if submit:
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
        response = requests.post("http://localhost:8080/api/churn/analise", json=payload)
        if response.status_code == 200:
            resultado = response.json()
            previsao = resultado['previsao']
            prob = resultado['probabilidade'] * 100

            st.divider()
            if previsao == "Vai cancelar":
                st.error("🚨 **ALERTA DE CHURN DETECTADO!**")
                st.metric(label="Probabilidade de Saída", value=f"{prob:.1f}%", delta="-Alto Risco")
            else:
                st.success("✅ **CLIENTE SEGURO**")
                st.metric(label="Probabilidade de Saída", value=f"{prob:.1f}%", delta="Baixo Risco")
        else:
            st.error(f"Erro na API Java: {response.status_code}")
    except Exception as e:
        st.error(f"Erro de conexão: Verifique se o Java está rodando. ({e})")