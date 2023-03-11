class Produto:

    imposto = 0.05
    id = 1000

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor + (valor * self.imposto)
        self.__id = Produto.id
        Produto.id = self.__id + 1

    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor
    
    @classmethod
    def id_produto(cls):
        return f'{cls.id}'

    def desconto(self, percentagem):
        self.__valor = self.__valor - (self.__valor * (percentagem/100))

    def __str__(self) -> str:
        return (f'Id: {self.id} - Nome: {self.nome} - Valor: {self.valor}')

    