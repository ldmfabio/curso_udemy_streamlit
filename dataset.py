import json
import pandas as pd
file = open('dados/vendas.json')
data = json.load(file)

#print(data)

df = pd.DataFrame.from_dict(data)

print(df)

file.close()