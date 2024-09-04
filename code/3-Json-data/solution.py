import json
import os

path = os.path.dirname(__file__)
file_path = os.path.join(path, 'dados.json')
with open(file_path, 'r') as file:
    data: list = json.load(file)

#print(data)

n = 0
media = 0
for dia in data:
    if dia['valor'] > 0:
        media += dia['valor']
        n += 1
media = media/n
num_dias = 0
for dia in data:
    if dia['valor'] > media:
        num_dias += 1
maximo = max(data, key=lambda x: x['valor'])
minimo = min(data, key=lambda x: x['valor'])


print(f'O maior valor é {maximo["valor"]} e o menor valor é {minimo["valor"]}')
print(f'O numero de dias com arrecadação acima da média é {num_dias}')
