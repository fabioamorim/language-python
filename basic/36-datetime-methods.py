from datetime import datetime
import timeit

now = datetime.now()

print(now)
# 2023-03-16 15:38:47.245894

print(datetime.today())
# 2023-03-16 15:39:14.776780

'''
0 - Monday
1 - Tuesday
2 - Wednesday
3 - Thursday
4 - Friday
5 - Saturdat
6 - Sunday
'''

print(now.weekday())
# 3

today_format = now.strftime('%d/%m/%y')

print(today_format)
# 16/03/23

today_format = now.strftime('%d/%m/%Y')

print(today_format)
# 16/03/2023

print(datetime.now().strftime('%d/%m/%Y'))
# 16/03/2023

birthday = datetime.strptime('10/04/1988', '%d/%m/%Y')

print(birthday)
# datetime 1988-04-10 00:00:00

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

print(tempo)