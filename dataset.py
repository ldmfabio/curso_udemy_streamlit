import json

file = open('dados/vendas.json')
data = json.load(file)

print(data)

file.close()