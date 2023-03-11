from produto import Produto
from employee import Employee

p1 = Produto('tv', 500)
p2 = Produto('monitor', 2000)

print(p1)

print(p1.id_produto())

employee1 = Employee('Fabio', 34, 111)

print(employee1)

employee1.about()
# This is about this employee