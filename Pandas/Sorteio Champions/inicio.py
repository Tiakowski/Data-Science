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

completo = False
pote = 0
potes = [pote1,pote2,pote3,pote4]
sorteados = 0
while not completo:
    print("----------------------------------------------------------------------------")
    print(f"Aperte uma tecla para sortear um time do pote {pote + 1}: \n")
    times_disponiveis = potes[pote].query('Sorteado == False')
    time_sorteado = times_disponiveis.sample()
    index = time_sorteado.query('Sorteado == False').index.tolist()
    potes[pote].at[index[0],'Sorteado']= True




    print(time_sorteado[['Time','Pais']].to_string(index=True)+"\n")
    
    print(f"Aperte uma tecla para sortear um grupo: \n")
    grupo_disponivel = False
    while not grupo_disponivel:
        nome_grupo_sorteado = random.choice(grupos_nomes)
        index_grupo_sorteado = grupos_nomes.index(nome_grupo_sorteado)
        grupo_sorteado = grupos[index_grupo_sorteado]
        paises = list(grupo_sorteado['Pais'])
        
        if grupo_sorteado.shape[0]  < 4: 
            print(f"Grupo sorteado: {nome_grupo_sorteado}\n")
            grupo_sorteado = pd.concat([grupo_sorteado, time_sorteado[['Time','Pais']]], axis=0,ignore_index=True)
            grupo_disponivel = True
    print(grupo_sorteado)
    
    print("----------------------------------------------------------------------------")
    if sorteados == 6 :
        completo = True
        pote+=1
    elif sorteados == 5:
        print("ooooi")
    else:    
        sorteados += 1
    # if comando == "1":
    #     completo = True



for i in grupos:
    print(i)

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

