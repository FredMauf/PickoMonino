from De import De;
print("Simulateur Pickmino")

de=De()
dico={}
dico[0]=0
dico[1]=0
dico[2]=0
dico[3]=0
dico[4]=0
dico[5]=0
dico['Asticot']=0
for i in range(2000):
    
    #print(de)
    dico[de.face]=dico[de.face]+1
    


liste_8={}


print(liste_8)

dic_asticot={}
for i in range(9):
    dic_asticot[i]=0

print(dic_asticot)

for i in range(10000):
    liste_8[1]=0
    liste_8[2]=0
    liste_8[3]=0
    liste_8[4]=0
    liste_8[5]=0
    liste_8['Asticot']=0
    for i in range(2):
        de.lancer()
        liste_8[de.face]=liste_8[de.face]+1

    dic_asticot[liste_8['Asticot']]=dic_asticot[liste_8['Asticot']]+1

print(dic_asticot)



