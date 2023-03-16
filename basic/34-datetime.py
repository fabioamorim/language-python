import datetime

print(dir(datetime))

print(datetime.MAXYEAR)
# 9999

print(datetime.MINYEAR)
# 1

print(datetime.datetime.now())
# 2023-03-16 15:01:07.531618 / repr=(year, month, day, hour, minute, second, microsencod)

inicio = datetime.datetime.now()

print(inicio)

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

evento = datetime.datetime(2024,1,5,0,1,1)

print(evento)
# 2024-01-05 00:01:01

birthday = '22/05/1988'

birthday = birthday.split('/')

print(birthday)
# ['22', '05', '1988']

birthday = datetime.datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))

print(birthday)
# 1988-05-22 00:00:00

print(birthday.year)
# 1988

print(birthday.day)
# 22