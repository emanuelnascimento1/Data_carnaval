import pandas as pd
# Definir url
def ajustar_url(ano):
    url = f"https://pt.wikipedia.org/wiki/Resultados_do_Carnaval_do_Rio_de_Janeiro_em_{ano}"
    return url
# Coletar dados
def coletar_dados(url):
    todas_tabelas = pd.read_html(url)
    return todas_tabelas


# Visualizar tabelas
def visualizar_tabelas(todas_tabelas):
    print("Tabelas disponíveis:")
    for i, tabela in enumerate(todas_tabelas):
        print(f"{i}: {tabela.columns.tolist()}")
# Escolher tabelas
def escolher_tabelas(tabelas):
    n_tabela = int(input("Digite o número da tabela que deseja visualizar: "))
    if n_tabela < 0 or n_tabela >= len(tabelas):
        print("Número de tabela inválido.")
        return None
    tabela_selecionada = tabelas[n_tabela]
    print(f"Tabela selecionada (primeiras 5 linhas):")
    print(tabela_selecionada.head())  # Exibe as primeiras 5 linhas da tabela
    return tabela_selecionada
# Salvar dados
# Main
ano = 2020
while ano <= 2024:
    print(f"Referente ao ano: {ano}")
    url = ajustar_url(ano)
    tabelas = coletar_dados(url)
    #visualizar_tabelas(tabelas)
    
    escolher_tabelas(tabelas)
    ano = ano + 1

