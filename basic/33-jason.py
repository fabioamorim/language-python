import json 

file = json.dumps(['produto', {'Playstantion 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(file))
print(file)