planilha = []

nomes = str(input("Digite seu nome:... "))
notas = input("Digite sua nota:... ")
planilha = (nomes, notas)

print(planilha)

print(type(notas))

notas = int(notas) #Não é a maneira mais comum de fazer, mas funciona

print(type(notas))