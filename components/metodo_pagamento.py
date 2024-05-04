import streamlit as st
from utils.pagamento import processar_pagamento

def mostrar_metodo_pagamento():
    """
    Função para exibir o conteúdo do método de pagamento.
    """
    st.write("Escolha seu método de pagamento:")
    metodo_pagamento = st.radio('', ['💳 Cartão de Crédito', '📱 Pix', '💵 À Vista'])
    if st.button('Pagar Agora'):
        processar_pagamento(metodo_pagamento.split()[1].lower())  # Pega apenas a palavra-chave do método

if __name__ == '__main__':
    mostrar_metodo_pagamento()
