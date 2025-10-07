class FolhaPagamento:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        print(self.nome, self.idade)

Funcionarios = FolhaPagamento("Matheus", 19)

Funcionarios.exibir()