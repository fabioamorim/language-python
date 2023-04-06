'''
Alerta!

Se o program python for executado com o parametro -O, nenhum assertion será validado. Ou seja, todas as suas validações
não irão funcionar.

'''

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0
    return a + b 

print(soma_numeros_positivos(-2, 4))

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

print(comer_fast_food('apple'))
# AssertionError: A comida precisa ser fast food