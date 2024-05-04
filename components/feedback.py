import streamlit as st

def mostrar_feedback():
    st.title("Feedback dos Clientes")

    # Campo para o usuário digitar o feedback
    feedback_usuario = st.text_area("Digite seu feedback aqui:")

    # Botão para enviar o feedback
    if st.button("Enviar Feedback"):
        st.write(f"Feedback do cliente: {feedback_usuario}")
        st.success("Obrigado pelo seu feedback! Ele é muito importante para nós.")
