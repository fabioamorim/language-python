'''
    Check reader, writer, DocReader and DocWriter form csv lib in python.

'''

from csv import reader, DictReader 
path = './files/lutadores.csv'

with open(path, encoding='utf-8') as arquivo:

    data = reader(arquivo)
    #data.__next__()
    next(data)
    for row in data:
        print(row)

print('\n')

with open(path, encoding='utf-8') as arquivo:

    data = DictReader(arquivo)

    for row in data:
        #print(row)
        print(f'Nome: {row["Nome"]}')