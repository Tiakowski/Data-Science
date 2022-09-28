import pandas as pd
#pd.set_option('display.max_rows', 5)

dataset = pd.read_csv('db.csv', sep= ';')

print(dataset[['Quilometragem','Valor']].describe())