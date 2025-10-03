#COMANDOS BÁSICOS

#Inicio
print("Hello World")
print(5+1)
print(5*"oi")
print("Oi""Te""Ba")
#----------------------------------------- 


#variaveis 
#INT -> Numeros inteiros
#FLOAT -> Numeros Quebrados
#STRING -> Para Textos
#-----------------------------------------


## Declarando uma varivel com Input
salario1 = float(input("Digite seu salario:... ")) #Obrigatoriamente o salario é FLOAT
print(f"Meu salario1 é {salario1}") #Imprimo na tela puxando a variavel
print(type(salario1)) ##Mostra para gente qual é o tipo da variavel salario

print("\n") #Pulo uma linha

salario2 = input("Digite seu salario:... ") #Salario é STRING, teria que converter depois
print(type(salario2)) ##Mostra para gente qual é o tipo da variavel salario
#----------------------------------------- 

##For
qts_de_alunos = int(input("Digite a quantidade de alunos:... "))
lista = []

for x in range(qts_de_alunos):
    nomes = str(input(f"Digite o nome do {x+1}:... "))
    notas1 = float(input(f"Digite sua {1}° nota:... "))
    notas2 = float(input(f"Digite sua {2}° nota:... "))
    medias = (notas1 + notas2)/2
    planilha = [nomes, medias]
    nomes = lista.append(planilha)


print(lista)