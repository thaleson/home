import streamlit as st

def processar_pagamento(metodo_pagamento):
    """
    Função de simulação de processamento de pagamento.
    """
    st.write(f'Processando pagamento via {metodo_pagamento}...')
    # Simulação de pagamento bem-sucedido
    st.success('Pagamento processado com sucesso!')
