# NOME: MATHEUS BEZERRA DOMMINGOS
# DATA: 04/10/2025
# OBJETIVO: FAZER UM PROGRAMA QUE VC CRIAR UMA PLANILHA E ALTERE OS DADOS

import pandas as pd

qts_de_fun = int(input("Digite a quantidade de funcionarios:... "))
lista = []


for x in range(qts_de_fun):

    nomes = str(input("Digite o Nome:... "))
    Idade = float(input("Digite Idade:... "))
    Salario = float(input(f"Digite Salario:... "))
    planilha = {'Nome': nomes, 'Idade': Idade, 'Salario': Salario}
    Folha = lista.append(planilha)



# Tipo da nossa tabela
df = pd.DataFrame(lista)
print("Arquivo criado com sucesso")

#define nome do arquivo
file_path = 'folha.csv'

#escrevendo os dados na folha_pagamento e criando o arquivo
df.to_csv(file_path, index=False) #index para não aparecer o indice no excel

#Perguntas dnv a quantidade de funcionarios novos
qts_de_fun = int(input("Digite a quantidade de funcionarios novos:... "))
lista_novos = []

for x in range(qts_de_fun):

    nomes = str(input("Digite o Nome:... "))
    Idade = float(input("Digite Idade:... "))
    Salario = float(input(f"Digite Salario:... "))
    planilha = {'Nome': nomes, 'Idade': Idade, 'Salario': Salario}
    Folha = lista_novos.append(planilha)

# Tipo da nossa tabela
df_novo = pd.DataFrame(lista_novos)

print("Arquivo criado com sucesso")
df_novo = pd.concat([df, df_novo], ignore_index=False)

# Agora você pode salvar o arquivo CSV com os dados atualizados
df_novo.to_csv(file_path, index=False)

