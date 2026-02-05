import numpy as np
import matplotlib.pyplot as plt
import uproot
import awkward as ak
from numpy import log as ln


#tutorial at: https://masonproffitt.github.io/uproot-tutorial/03-trees/index.html

############################################################
#On importe les fichier root
############################################################


file_csi = uproot.open('csi-cube.root')           #Importation des fichier
#filePb= uproot.open('Pb1.root')
#fileG=uproot.open('Gant1.root')
#filed2=uproot.open('detecteur2gant.root')

#####################################################################

keys_csi=file_csi.keys()  #Keys prend la forme d'une liste contenant les différents nom des  detecteurs 
print(keys_csi)

class_csi=file_csi.classnames() #En affichant class1 on peut voir a quoi correspond chaque noms des repertoires ex {'Detector/CsI-cube;1':'TNtuple'} tuple : liste de données qui sont pas modifiable
print(class_csi)

tree_csi = file_csi['Detector/CsI-cube'] 
tree_csi.keys()   #On importe les différentes données ("énergie,masse,ID....") sous formes de liste.
print(tree_csi.keys())

branches_csi=tree_csi.arrays() #Branche est un tableaux conetenant les données; Array[Nbproton: 2, Pronton_edep: [10.8, ... -1, 1]]
branches_csi['Edep'] #Tableau des énergies 
print(branches_csi['Edep']) #Affiches le tableau d'énergoies


#keysPb=filePb.keys()
#classPb=filePb.classnames()
#treePb = filePb['Detector/CdTe-cubePb'] 
#treePb.keys()
#branchesPb=treePb.arrays()
#branchesPb['Edep']


#classG=fileG.classnames()
#treeG = fileG['Detector/CdTe-25'] 
#treeG.keys()
#branchesG=treeG.arrays()
#branchesG['Edep']

#keysd2=filed2.keys()
#classd2=filed2.classnames()
#treed2= filed2['Detector/CsI2'] 
#branchesd2=treed2.arrays()
#branchesd2['Edep']


##########################################################################################################
#Histograms pour une entrée de 1e7
##########################################################################################################


plt.yscale('log')  #Affiche en échelle logarithmique selon l'axe des y
[y,x,z]=plt.hist(branches_csi['Edep'],bins=500,range=(0,1.2)) # x est le tableau des énergies, y le nombre de coups et z est un caractère donnant le types des élements du tableau correpondant au fichier file
#[yg,xg,zg]=plt.hist(branchesG['Edep'],bins=500,range=(0, 0.5)) #bins représente le nombre de canaux, range#=(0,0.5) permet de choisir l'intervalle des valeurs choisis
#[ypb,xpb,zpb]=plt.hist(branchesPb['Edep'],bins=500)



#Ly,Lyg,Lypb=y.tolist(),yg.tolist(),ypb.tolist() #On tranforme les tableau en liste pour facilité l'utilisa#tion
#Lx,Lxg,Lxpb=x.tolist(),xg.tolist(),xpb.tolist()


#Lx.pop(499),Lxg.pop(499),Lxpb.pop(499)   #Les tailles des deux listes sont différents, on supprime donc la coordonnées qui n'a pas le nombre de coups associés qui est donc la dernière.

#[ydg,xdg,zdg]=plt.hist(branchesd2['Edep'],bins=500)
#Lxdg=xdg.tolist()
#Lxdg.pop(0)
#Lydg=ydg.tolist()


################################################
#Calcul du taux d'absorption
#################################################

#Xg=[]   #Xg est une liste vide
#Xpb=[]
#Ag=[]
#Apb=[]

####################################
#Taux d'absorption
####################################

#for k in range(1,len(Lypb)):           #On parcour la liste. len(Lypb) : taille de la liste
   # Apb.append(Lypb[k]/Ly[k])      #On ajoute a la liste Apb la taux d'absorption
   # Xpb.append(Lxpb[k])            

#################################################################
#Calcul du taux d'atténuation du Pb  pour une épaisseur de 50um
##################################################################

#upb=[]
#for k in range(1,len(Lypb)):
   # upb.append(-float(ln(Lypb[k]/Ly[k]))/(11.3*0.05))




##########################################################################
#Exporter les listes sur excel
#pip install openpyxl
#pip install xlwt

##########################################################################"
#import pandas as pd
#import xlwt
#from xlwt import Workbook

#col1 = "Edep"          #Nom de la première colonne case A1
#col2 = "Nombre de coups"
#data = pd.DataFrame({col1:Lyg,col2:Lxg}) #Data prend la valeur des données voulue dans chaque colonne : col1 prend les valeurs de la liste Lyg donc le nombre de coups dans le gant).

#data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False) #Création d'un fichier excel du nom sample_data


#####################################
#Affichage des courbes
#####################################

plt.figure(2)   #Nom de la figure 
plt.title('Nombre de coup pour une entrée de spectre plat') 
plt.xlabel('Edep (MeV)')  #titre de l'axe des abscisses
plt.ylabel('nombre de particules')  #Titre de l'axe des ordonnées
plt.yscale('log')  #Affiche en échelle logarithmique selon l'axe des y
#plt.plot(Lx,Ly, linestyle='-', color='pink',label='Plomb')
plt.hist(branches_csi['Edep'],bins=100,range=(0,2))
plt.legend(loc="lower right") #Position de la légende

################################ Taux d'absorption  ###############################################

#plt.figure(3)
#plt.title('Comparaison des taux d absorption') 
#plt.xlabel('Edep (MeV)')
#plt.ylabel('Taux d absroption (I/Io)')
#plt.plot(Xpb,Apb,label='Plomb 50um', color='purple')
#plt.legend(loc="lower right")


#############################Taux d'atténuation ############################################

#plt.figure(4)
#plt.title('Taux d atténuation') 
#plt.xlabel('Edep (MeV)')
#plt.ylabel('Taux d atténuation μ (cm2/g)')
#plt.plot(Xpb,upb,label='Taux d atténuation du Pb 50um',color='plum')
#plt.legend(loc="upper right")

plt.show()
