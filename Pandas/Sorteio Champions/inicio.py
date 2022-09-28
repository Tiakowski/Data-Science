import pandas as pd
import random


pote1 = [
    {'Time': 'Real Madrid', 'Pais':'Espanha','Pote':1, 'Sorteado': False},
    {'Time': 'Frankfurt', 'Pais':'Alemanha','Pote':1,'Sorteado': False},
    {'Time': 'Manchester City', 'Pais':'Inglaterra','Pote':1,'Sorteado': False},
    {'Time': 'Milan', 'Pais':'Italia','Pote':1,'Sorteado': False},
    {'Time': 'Bayern', 'Pais':'Alemanha','Pote':1,'Sorteado': False},
    {'Time': 'PSG', 'Pais':'França','Pote':1,'Sorteado': False},
    {'Time': 'Porto', 'Pais':'Portugal','Pote':1,'Sorteado': False},
    {'Time': 'Ajax', 'Pais':'Holanda','Pote':1,'Sorteado': False}]

pote2 = [
    {'Time': 'Liverpool', 'Pais':'Inglaterra','Pote':2,'Sorteado': False},
    {'Time': 'Chelsea', 'Pais':'Inglaterra','Pote':2,'Sorteado': False},
    {'Time': 'Barcelona', 'Pais':'Espanha','Pote':2,'Sorteado': False},
    {'Time': 'Juventus', 'Pais':'Italia','Pote':2,'Sorteado': False},
    {'Time': 'Atletico', 'Pais':'Espanha','Pote':2,'Sorteado': False},
    {'Time': 'Sevilla', 'Pais':'Espanha','Pote':2,'Sorteado': False},
    {'Time': 'Leipzig', 'Pais':'Alemanha','Pote':2,'Sorteado': False},
    {'Time': 'Tottenham', 'Pais':'Inglaterra','Pote':2,'Sorteado': False}]

pote3 = [
    {'Time': 'Dortmund', 'Pais':'Alemanha','Pote':3,'Sorteado': False},
    {'Time': 'Salzburg', 'Pais':'Austria','Pote':3,'Sorteado': False},
    {'Time': 'Shakhtar Donetsk', 'Pais':'Ucrania','Pote':3,'Sorteado': False},
    {'Time': 'Inter', 'Pais':'Italia','Pote':3,'Sorteado': False},
    {'Time': 'Napoli', 'Pais':'Italia','Pote':3,'Sorteado': False},
    {'Time': 'Benfica', 'Pais':'Portugal','Pote':3,'Sorteado': False},
    {'Time': 'Sporting', 'Pais':'Portugal','Pote':3,'Sorteado': False},
    {'Time': 'Leverkusen', 'Pais':'Alemanha','Pote':3,'Sorteado': False}]

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

pote1 = pd.DataFrame(pote1)
pote2 = pd.DataFrame(pote2)
pote3 = pd.DataFrame(pote3)
pote4 = pd.DataFrame(pote4)

GrupoA = pd.DataFrame(columns=['Time','Pais'])
GrupoB = pd.DataFrame(columns=['Time','Pais'])
GrupoC = pd.DataFrame(columns=['Time','Pais'])
GrupoD = pd.DataFrame(columns=['Time','Pais'])
GrupoE = pd.DataFrame(columns=['Time','Pais'])
GrupoF = pd.DataFrame(columns=['Time','Pais'])
GrupoG = pd.DataFrame(columns=['Time','Pais'])
GrupoH = pd.DataFrame(columns=['Time','Pais'])

grupos = [GrupoA, GrupoB, GrupoC, GrupoD, GrupoE, GrupoF, GrupoG, GrupoH]
grupos_nomes = ["Grupo A","Grupo B", "Grupo C", "Grupo D", "Grupo E", "Grupo F", "Grupo G","Grupo H"]
    

def sortear():
    numero = random.randrange(7)
    return numero

completo = False
pote = 0
potes = [pote1,pote2,pote3,pote4]

while not completo:
    print("----------------------------------------------------------------------------")
    comando = input(f"Aperte uma tecla para sortear um time do pote {pote + 1}: \n")
    numero_sorteado = sortear()
    time_sorteado = potes[pote].iloc[[numero_sorteado]]
    potes[pote].at[numero_sorteado,'Sorteado']= True
    print(time_sorteado[['Time','Pais']].to_string(index=False)+"\n")


    
    comando2 = input(f"Aperte uma tecla para sortear um grupo: \n")
    disponivel = False
    while not disponivel:
        grupo_sorteado = sortear()
        paises = list(grupos[grupo_sorteado]['Pais'])
        
        if grupos[grupo_sorteado].shape[0]  < 4: 
            print(f"Grupo sorteado: {grupos_nomes[grupo_sorteado]}")
            #grupos[grupo_sorteado] = pd.concat(time_sorteado[['Time','Pais']])
            grupos[grupo_sorteado] = pd.concat([grupos[grupo_sorteado], time_sorteado[['Time','Pais']]], axis=0,ignore_index=True)
            disponivel = True
    print(grupos[grupo_sorteado])
    
    print("----------------------------------------------------------------------------")
    if pote < 3:
        pote+=1
    else:
        pote=0        

    if comando == "1":
        completo = True


# print(pote_vez.to_string(index=False))

#pote_vez = pote1.query(f'Pote == {pote}')

# print(pote1['Time'])

# while not completo:
#     input("\n Aperta uma tecla para selecionar um time: \n")
#     time = sortear()
#     print("Resultado:")
#     print(pote1.iloc[[time]])
    
#     input("Sortear grupo:")
#     grupo = sortear()

# Pote = 4
# teste = pote1.query(f'Pote == {Pote}')
# print(teste['Time'])

# paises = pote1['Pais']
# print(paises)
    
# print(paises.drop_duplicates())
    


# select = pote3.Pais == 'Italia'
# print(pote3[select])

#print(pote3.query('Pais == "Italia"'))

