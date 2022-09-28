import pandas as pd

pote4 = [
    {'Time': 'Rangers', 'Pais':'Escocia','Pote':4,'Sorteado': False},
    {'Time': 'Dinamo Zagreb', 'Pais':'Croacia','Pote':4,'Sorteado': False},
    {'Time': 'Marseille', 'Pais':'França','Pote':4,'Sorteado': False},
    {'Time': 'Copenhagen', 'Pais':'Dinamarca','Pote':4,'Sorteado': False},
    {'Time': 'Brugge', 'Pais':'Belgica','Pote':4,'Sorteado': False},
    {'Time': 'Celtic', 'Pais':'Escocia','Pote':4,'Sorteado': False},
    {'Time': 'Viktoria Plzen', 'Pais':'Tchequia','Pote':4,'Sorteado': False},
    {'Time': 'Maccabi Haifa', 'Pais':'Israel','Pote':4,'Sorteado': False}
]

pote4 = pd.DataFrame(pote4)

paises = list(pote4['Pais'])
print(paises)
