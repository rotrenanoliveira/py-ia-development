import json

import requests
import streamlit as st

# Título da Aplicação
st.title("Modelo Predição de Salário - Regressão Polinomial")

# Inputs do usuário
st.write("Quantos meses o profissional está na empresa?")
tempo_na_empresa = st.slider("Meses", min_value=1, max_value=120, value=60, step=1)

st.write("Qual o nível do profissional na empresa?")
nivel_na_empresa = st.slider("Nível", min_value=1, max_value=10, value=5, step=1)

# Preparar dados para API
input_features = {
    "tempo_na_empresa": tempo_na_empresa,
    "nivel_na_empresa": nivel_na_empresa,
}

# Criar um botão e capturar um evento deste botão para disparar a API
if st.button("Estimar Salário"):
    res = requests.post(
        "http://localhost:8000/predict", data=json.dumps(input_features)
    )

    res_json = json.loads(res.text)
    salario_em_reais = round(res_json["salario_em_reais"], 2)

    st.subheader(f"Salário estimado: R${salario_em_reais}")
