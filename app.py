import streamlit as st
from PIL import Image
from components.metodo_pagamento import mostrar_metodo_pagamento
from navegacao.navegacao import mostrar_abas

def main():
    st.title('E-commerce de Contratação de Mão de Obra')
    st.sidebar.header('Detalhes da Empresa')
    st.sidebar.write("Somos uma empresa especializada em oferecer mão de obra temporária e efetiva em diversas áreas.")

    # Carregar e exibir imagens
    imagens = {
        'Embalador': 'embalador.jpg',
        'Pedreiro': 'pedreiro.jfif',
        'TI': 'TI.jpg'
    }

    for nome, arquivo in imagens.items():
        imagem = Image.open(f'assets/{arquivo}')
        st.image(imagem, caption=nome, use_column_width=True)

    # Seção: Detalhes sobre os Serviços
    st.subheader("Detalhes sobre os Serviços")
    st.write("""
    Oferecemos serviços especializados em diversas áreas, incluindo:
    - **Embalagem**: Nossos embaladores garantem que seus produtos sejam embalados com segurança e eficiência.
    - **Pedreiro**: Contrate nossos pedreiros para projetos de construção e reforma em sua residência ou empresa.
    - **TI (Tecnologia da Informação)**: Contamos com profissionais de TI qualificados para atender às suas necessidades tecnológicas.
    """)

    # Seção: Método de Pagamento
    st.subheader("Método de Pagamento")
    mostrar_metodo_pagamento()

    # Mostrar abas de feedback e classificação
    mostrar_abas()

    # Rodapé
    st.sidebar.write("Desenvolvido por Thaleson Silva")

if __name__ == '__main__':
    main()
