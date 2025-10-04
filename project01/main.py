# NOME: MATHEUS BEZERRA DOMMINGOS
# DATA: 04/10/2025
# OBJETIVO: FAZER UM PROGRAMA QUE CRIE E LEIA UMA PLANILHA

#IMPORTANTO A LIB. PANDAS -> MANIPULLAÇÃO DE DADOS
import pandas as pd

#igual o conceito de dicionario, dados da tabela
planilha = {
    'NOME': ['Matheus', 'Otavio', 'Luiz', 'Gabriel'],
    'IDADE': [19, 18, 19, 20],
    'SALARIO': [1600, 3000, 1400, 0]
}

# Tipo da nossa tabela
df = pd.DataFrame(planilha)
print("Arquivo criado com sucesso")

#define nome do arquivo
file_path = 'folha_pagamento2.xlsx'

#escrevendo os dados na folha_pagamento
df.to_excel(file_path, index=False) #index para não aparecer o indice no excel


print(planilha)