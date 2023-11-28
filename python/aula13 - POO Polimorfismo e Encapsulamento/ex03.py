"""
Criando uma Classe:
Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado apresentar que imprime uma mensagem de apresentação, incluindo o nome e a idade da pessoa.

Herança:
Crie uma classe chamada Estudante que herda da classe Pessoa. Adicione um atributo adicional chamado curso à classe Estudante. Atualize o método apresentar para incluir também o curso do estudante.

Encapsulamento:
Modifique a classe Pessoa para tornar os atributos nome e idade privados. Adicione métodos getter e setter para acessar e modificar esses atributos.

Polimorfismo:
Crie duas classes, Cachorro e Gato, ambas com um método fazer_som. O método fazer_som na classe Cachorro deve imprimir "Au Au", enquanto na classe Gato deve imprimir "Miau".

Composição:
Crie uma classe chamada Carro com atributos como modelo e ano. Em seguida, crie uma classe chamada Pessoa com atributos como nome e carro (um objeto da classe Carro). Isso representa a composição, onde uma pessoa tem um carro.

Métodos Estáticos:
Adicione um método estático à classe Pessoa que calcula a idade média de um grupo de pessoas.

"""

from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, novo_idade):
        self.__idade = novo_idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome} e tenho {self.__idade} anos!")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos!")
        print(f"Atualmente estou cursando {self.curso}!")
