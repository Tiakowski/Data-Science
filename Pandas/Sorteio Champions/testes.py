# import pandas as pd
import random

# pote4 = [
#     {'Time': 'Rangers', 'Pais':'Escocia','Pote':4,'Sorteado': False},
#     {'Time': 'Dinamo Zagreb', 'Pais':'Croacia','Pote':4,'Sorteado': False},
#     {'Time': 'Marseille', 'Pais':'França','Pote':4,'Sorteado': False},
#     {'Time': 'Copenhagen', 'Pais':'Dinamarca','Pote':4,'Sorteado': False},
#     {'Time': 'Brugge', 'Pais':'Belgica','Pote':4,'Sorteado': False},
#     {'Time': 'Celtic', 'Pais':'Escocia','Pote':4,'Sorteado': False},
#     {'Time': 'Viktoria Plzen', 'Pais':'Tchequia','Pote':4,'Sorteado': False},
#     {'Time': 'Maccabi Haifa', 'Pais':'Israel','Pote':4,'Sorteado': False}
# ]

# pote4 = pd.DataFrame(pote4)

# paises = list(pote4['Pais'])
# print(paises)

# sorteio = pote4.sample()
# print(sorteio)
# def soma(numero=4):
#     print(numero)

# soma(8)

grupos_nomes = ["Grupo A","Grupo B", "Grupo C", "Grupo D", "Grupo E", "Grupo F", "Grupo G","Grupo H"]  
sorteio = random.choice(grupos_nomes)
index = grupos_nomes.index(sorteio)
print(sorteio)
print(index)