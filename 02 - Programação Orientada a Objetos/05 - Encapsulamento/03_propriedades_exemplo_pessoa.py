class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")
