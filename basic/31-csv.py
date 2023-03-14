from csv import writer, DictWriter

path = './files/test.csv'
path_2 = './files/test_2.csv'

lista = ['Number1', 'Number2']

with open(path, 'w') as file:

    writer_csv = writer(file)

    writer_csv.writerow(lista)

    for i in range(10):
        writer_csv.writerow([i, i*2])

with open(path_2, 'w', newline='', encoding='utf-8') as file_2:

    fieldnames = ['Number1', 'Number2']

    writer_csv = DictWriter(file_2, fieldnames=fieldnames)
    writer_csv.writeheader()

    for i in range(10):
        writer_csv.writerow({'Number1': (i+1)*100, 'Number2': i+1})
