import pickle

class Animal:

    def __init__(self, nome):
        self._nome = nome 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def comer(self):
        print(f'{self._nome} está comendo ...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando ...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')

felix = Gato('Felix')
pluto = Cachorro('Pluto')

path = './files/'

with open(f'{path}animais.pickle', 'wb') as file:
    pickle.dump((felix, pluto), file)

with open(f'{path}animais.pickle', 'rb') as file:
    gato, cachorro = pickle.load(file)

    print(gato.nome, cachorro.nome)