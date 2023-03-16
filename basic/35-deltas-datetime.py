'''
delta = diferença entre data inicial e data final
'''

from datetime import datetime, timedelta

data_hoje = datetime.now()

outra_data = datetime(2024,11,1,0)

tempo_para_evento = outra_data - data_hoje

print(type(data_hoje))
# <class 'datetime.datetime'>

print(type(outra_data))
# <class 'datetime.datetime'>

print(type(tempo_para_evento))
# <class 'datetime.timedelta'>

print(tempo_para_evento)
# 595 days, 8:31:49.741315

print(tempo_para_evento.days)
# 595

print(tempo_para_evento.total_seconds())
# 51438739.312291

new_time = timedelta(days=3)

print(new_time)

tempo_para_evento += new_time

print(tempo_para_evento.days)
# 598