def registrar_classificacao(classificacao):
    """
    Função para registrar a classificação do site.
    """
    if 1 <= classificacao <= 10:
        # Aqui você pode adicionar lógica para armazenar a classificação em um banco de dados, arquivo, etc.
        # Neste exemplo, apenas exibimos a classificação no console.
        print(f"A classificação do site é: {classificacao}")
    else:
        print("Erro: A classificação deve estar entre 1 e 10.")
