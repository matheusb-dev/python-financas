# NOME: MATHEUS BEZERRA DOMINGOS
# DATA: 07/10/2025
# OBJETIVO: Um objeto "ContaBancária" pode ter atributos como "saldo" e métodos como "depositar" e "sacar".

class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor

    def exibir(self):
        print(self.saldo)
    
Matheus = ContaBancaria(50)


Matheus.depositar(80)

Matheus.exibir()

        