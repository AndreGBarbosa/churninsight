# 📊 ChurnInsight - MVP Hackathon

> **Status do Projeto:** ✅ Concluído e Integrado
> **Setor:** Serviços e Assinaturas (Telecom, Fintech, Streaming)

## 🎯 O Desafio de Negócio

Empresas que dependem de receita recorrente sofrem com o **Churn** (cancelamento de clientes). O mercado valida que manter um cliente fiel é muito mais barato do que conquistar um novo.

O objetivo do **ChurnInsight** é oferecer uma "bola de cristal" baseada em dados: uma solução capaz de prever, com base no comportamento de uso e histórico financeiro, se um cliente está propenso a cancelar o contrato. Isso permite que times de Marketing e Sucesso do Cliente ajam preventivamente.

---

## 🛠️ Arquitetura da Solução

O projeto foi desenvolvido em uma **colaboração estreita entre os times de Data Science e Back-end**, resultando em uma arquitetura de microsserviços:

1. **O "Cérebro" (AI Service):** Um microserviço em **Python (Flask)** que carrega o modelo preditivo e processa os dados.
2. **O "Gerente" (Back-end API):** Uma API robusta em **Java (Spring Boot)** que gerencia as requisições, valida regras de negócio e integra com a IA.
3. **A "Vitrine" (Dashboard):** Uma interface visual em **Streamlit** para visualização rápida dos resultados.

---

## 📈 A Evolução do Back-end (Do MVP à Versão Final)

O desenvolvimento do Back-end seguiu uma jornada incremental de superação de desafios técnicos:

### Fase 1: O MVP Básico (5 Features)

Inicialmente, a API foi projetada para receber apenas 5 dados essenciais (`tempo de contrato`, `fatura`, `minutos de uso`, `total de chamadas`, `idade do equipamento`).

* **Desafio:** Ao integrar com o modelo oficial de Data Science, enfrentamos um *Feature Mismatch*. O modelo esperava 100 colunas, mas o Back-end enviava apenas 5, gerando erros de compatibilidade.
* **Solução Rápida:** O time de Back-end desenvolveu um script (`criar_modelo.py`) para treinar um modelo "Mock" local, permitindo que a API continuasse sendo desenvolvida sem bloqueios enquanto o modelo oficial era ajustado.

### Fase 2: Expansão e Engenharia de Features (13 Features)

Para aumentar a precisão da previsão, expandimos o escopo. A versão final não usa apenas dados brutos, mas sim um **Pipeline de Dados**.

* **Refatoração:** Os DTOs (`Data Transfer Objects`) no Java foram atualizados com **Lombok** para suportar 13 variáveis.
* **Resiliência:** Implementamos um mecanismo de *fallback* no Python. Se o modelo principal falhar ou tiver incompatibilidade de versão, o sistema carrega automaticamente um modelo de backup seguro, garantindo que a API nunca pare de responder (SLA).

---

## 🖥️ O Dashboard Visual (Front-end)

Para democratizar o acesso à inteligência artificial, criamos um dashboard interativo utilizando **Streamlit**.

* **Objetivo:** Permitir que gestores testem a ferramenta sem precisar escrever código.
* **Funcionalidade:** O dashboard consome a API Java (na porta 8080), que por sua vez consulta a IA. Ele exibe alertas visuais:
* 🔴 **Alerta de Risco:** Probabilidade alta de cancelamento.
* 🟢 **Cliente Seguro:** Probabilidade baixa de cancelamento.



---

## 🧪 Qualidade de Código e Testes Automatizados

A confiabilidade da integração foi garantida através da classe de testes `ChurninsightApplicationTests.java`.

Não se trata apenas de testes unitários simples. Criamos um **Teste de Integração Automatizado** que:

1. Sobe o contexto do Spring Boot.
2. Injeta o `ChurnService`.
3. Cria um cenário real com um cliente fictício preenchido com as 13 variáveis.
4. **Realiza uma chamada real** ao microsserviço Python.
5. Valida (Asserts) se a resposta contém uma previsão de texto e uma probabilidade numérica.

> Isso garante que qualquer alteração no código que quebre a comunicação com a IA seja detectada imediatamente antes do deploy.

---

## 🔑 Fatores que Influenciam o Resultado (Features)

O modelo final analisa 13 fatores comportamentais divididos em 3 pilares para decidir se o cliente vai cancelar:

### 1. Perfil e Contrato

* **`months` (Tempo de Contrato):** Clientes novos tendem a ser mais voláteis.
* **`rev_Mean` (Fatura Média):** Valor gasto mensalmente.
* **`avgrev` (Histórico de Receita):** Média de gastos ao longo da vida do cliente.
* **`eqpdays` (Idade do Equipamento):** Equipamentos antigos podem gerar insatisfação.
* **`eqp_age_index`:** Índice calculado da depreciação do equipamento.

### 2. Comportamento de Uso

* **`mou_Mean` (Minutos de Uso):** Queda no uso geralmente precede o cancelamento.
* **`totcalls` (Total de Chamadas):** Nível de atividade.
* **`avgmou` (Média Histórica):** Comparativo de uso atual vs. passado.
* **`rev_per_minute`:** Custo benefício para o cliente.
* **`calls_per_month`:** Frequência de utilização.

### 3. Satisfação e Qualidade

* **`custcare_Mean` (Chamadas ao Suporte):** Alto volume indica problemas não resolvidos.
* **`drop_vce_Mean` (Chamadas Caídas):** Falhas técnicas da operadora.
* **`blck_vce_Mean` (Chamadas Bloqueadas):** Erros de rede.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Java 17+
* Python 3.10+ e bibliotecas (`flask`, `pandas`, `scikit-learn`, `joblib`, `streamlit`)

### Passo 1: Iniciar a Inteligência Artificial

```bash
cd churn-ia
python app.py

```

### Passo 2: Iniciar a API Java

Execute a classe principal `ChurninsightApplication` na sua IDE.

### Passo 3: Abrir o Dashboard

```bash
cd churn-ia
streamlit run dashboard.py

```

---

### 🤝 Colaboração

Este projeto é fruto da união entre as disciplinas de **Desenvolvimento de Software** e **Ciência de Dados**, demonstrando como modelos matemáticos complexos podem ser transformados em produtos de software utilizáveis e escaláveis.