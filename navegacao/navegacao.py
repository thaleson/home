import streamlit as st
from components.feedback import mostrar_feedback
from utils.classificacao import registrar_classificacao

# Adicionando abas para feedback e classificação
def mostrar_abas():
    app_mode = st.sidebar.selectbox("Escolha uma opção", ["Home", "Feedback", "Classificação"])

    # Aba Feedback
    if app_mode == "Feedback":
        mostrar_feedback()

    # Aba Classificação do Site
    elif app_mode == "Classificação":
        classificacao = st.slider("Em uma escala de 1 a 10, qual é a sua classificação para o site?", 1, 10)
        if st.button("Enviar Classificação"):
            registrar_classificacao(classificacao)
