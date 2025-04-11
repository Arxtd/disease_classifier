from sklearn import tree

# Sintomas: febre, tosse, fadiga, dor_cabeca, sede_excessiva, visao_turva, perda_olfato_paladar, pressao_alta
caracteristicas = [
    [1, 1, 1, 1, 0, 0, 0, 0],  # Gripe
    [0, 0, 1, 0, 1, 1, 0, 0],  # Diabetes Tipo 2
    [0, 0, 1, 1, 0, 1, 0, 1],  # Hipertensão
    [1, 1, 1, 0, 0, 0, 1, 0],  # COVID-19
]

doencas = [0, 1, 2, 3]

clf = tree.DecisionTreeClassifier()
clf.fit(caracteristicas, doencas)


meus_sintomas = [1, 1, 1, 0, 0, 0, 0, 0]
previsao = clf.predict([meus_sintomas])

mapper_doenca = {0: "Gripe", 
                 1: "Diabetes tipo 2", 
                 2: "Hipertensão", 
                 3: "COVID-19"}

print("Você provavelmente está com: ", mapper_doenca[previsao[0]])