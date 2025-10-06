# NOME: MATHEUS BEZERRA DOMMINGOS
# DATA: 04/10/2025
# OBJETIVO: LE A PLANILHA E NA HORA DE REESCREVER IGNORA OS DADOS ANTIGOS

import pandas as pd

#data frame
df = pd.read_csv('folha.csv')

print(df)

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
df = pd.DataFrame(lista_novos)

print("Arquivo criado com sucesso")
df = pd.concat([df], ignore_index=False)

#define nome do arquivo
file_path = 'folha.csv'

# Agora você pode salvar o arquivo CSV com os dados atualizados
df.to_csv(file_path, index=False)
