"""
Decorators

"""

# Higher order functions - Funções de maior grandeza

def somar(a, b):
    return a+b

def diminuir(a, b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a, b):
    return a/b 

def calcular(num1, num2, funcao):
    return funcao(num1,num2)

print(calcular(2,2, somar))
print(calcular(2,2, diminuir))
print(calcular(2,2, multiplicar))
print(calcular(2,2, dividir))

# Nested Functions - Funções Aninhadas

def test1(name):
    def test1():
        return f'Hello {name}'
    return test1() + ' ,Welcome!!'

print(test1('Fulano'))
# Hello Fulano ,Welcome!!

# Decorators

def be_good(fun):
    def action():
        print("Thank you so much!")
        fun()
        print("Have a nice day!")
    return action

def hello():
    print('Hello my friend')

teste = be_good(hello())
