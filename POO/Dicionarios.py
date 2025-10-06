# NOME: MATHEUS BEZERRA DOMMINGOS
# DATA: 04/10/2025
# OBJETIVO: APRENDENDO SOBRE DICIONARIO

import pandas as pd

qts_de_fun = int(input("Digite a quantidade de funcionarios:... "))
lista = []


for x in range(qts_de_fun):

    nomes = str(input("Digite o Nome:... "))
    Idade = float(input("Digite Idade:... "))
    Salario = float(input(f"Digite Salario:... "))

    #Dicionario que defini as linhas da tabela
    planilha = {
        'Nome': nomes, 
        'Idade': Idade, 
        'Salario': Salario
    }

    lista.append(planilha)



# Tipo da nossa tabela
df = pd.DataFrame(lista)
print("Arquivo criado com sucesso")

#define nome do arquivo
file_path = 'folha.csv'

#escrevendo os dados na folha_pagamento e criando o arquivo
df.to_csv(file_path, index=False) #index para não aparecer o indice no excel

