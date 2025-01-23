import pandas as pd
import os

# Definir URL
def ajustar_url(ano):
    return f"https://pt.wikipedia.org/wiki/Resultados_do_Carnaval_do_Rio_de_Janeiro_em_{ano}"

# Coletar dados
def coletar_dados(url):
    try:
        return pd.read_html(url)
    except Exception as e:
        print(f"Erro ao coletar dados da URL {url}: {e}")
        return None

# Visualizar tabelas
def visualizar_tabelas(todas_tabelas):
    print("Tabelas disponíveis:")
    for i, tabela in enumerate(todas_tabelas):
        print(f"{i}: {tabela.columns.tolist()}")

# Escolher tabelas
def escolher_tabelas(tabelas):
    try:
        n_tabela = int(input("Digite o número da tabela que deseja visualizar: "))
        if n_tabela < 0 or n_tabela >= len(tabelas):
            print("Número de tabela inválido.")
            return None
        return tabelas[n_tabela]
    except Exception as e:
        print(f"Erro ao selecionar a tabela: {e}")
        return None

# Salvar escolas
def salvar_escolas(tabela_selecionada):
    arquivo = "escolas_samba.csv"
    
    # Verificar se a coluna 'Escola' existe
    if "Escola" not in tabela_selecionada.columns:
        print("A coluna 'Escola' não está presente na tabela selecionada.")
        return

    # Visualizar colunas da tabela antes de salvar
    print(f"As colunas da tabela selecionada são: {tabela_selecionada.columns.tolist()}")
    aprovacao = input("Deseja aprovar a inclusão dessa tabela no arquivo? (s/n): ").strip().lower()
    if aprovacao != 's':
        print("Tabela não aprovada para inclusão.")
        return

    # Verificar se o arquivo já existe
    if os.path.exists(arquivo):
        escolas_salvas = pd.read_csv(arquivo)
    else:
        escolas_salvas = pd.DataFrame(columns=["Escola"])
    
    # Filtrar apenas a coluna 'Escola'
    escolas_revisao = tabela_selecionada[["Escola"]]
    
    # Identificar novas escolas
    novas_escolas = escolas_revisao[~escolas_revisao["Escola"].isin(escolas_salvas["Escola"])]

    # Salvar apenas as novas escolas
    if not novas_escolas.empty:
        try:
            novas_escolas.to_csv(arquivo, mode='a', index=False, header=not os.path.exists(arquivo), encoding='utf-8')
            print(f"As novas escolas foram adicionadas ao arquivo '{arquivo}'.")
        except Exception as e:
            print(f"Erro ao salvar no arquivo: {e}")
    else:
        print("Nenhuma escola nova para adicionar.")

# Main
ano = 1961
while ano <= 2024:
    print(f"Coletando dados para o ano: {ano}")
    url = ajustar_url(ano)
    tabelas = coletar_dados(url)

    if tabelas:
        visualizar_tabelas(tabelas)  # Mostrar tabelas disponíveis
        tabela_selecionada = escolher_tabelas(tabelas)
        if tabela_selecionada is not None:
            salvar_escolas(tabela_selecionada)
        else:
            print(f"Nenhuma tabela válida para o ano {ano}.")
    else:
        print(f"Nenhuma tabela encontrada para o ano {ano}.")
    ano += 1
