# NOME: MATHEUS BEZERRA DOMINGOS
# DATA: 03/10/2025
# OBETIVO: FAZER UM PROGRAMA QUE CRIA E LEIA UMA PLANILHA NO EXCEL
# BIBLIOTECA: PANDAS

# PANDAS É UMA LIB. DE MANIPULAÇÃO DE DADOS
import pandas as pd

#dados da tabela
planilha = {
    'Nomes': ['Matheus', 'Otavio', 'Gabriel', 'Luiz'],
    'Idade': [19, 18, 20, 19],
    'Salarios': [1600, 3000, 0, 1400],
}

#defini o tipo tabela
df = pd.DataFrame(planilha) #uso o DataFrame para manipulação de dados Bidmencional

print("Arquivo criado com sucesso")
print(planilha)