import numpy as np
import math 
#-------------------------------------
def determinantMatriceTriangulaire(matrice):
    #taille = np.size(matrice)# si 3 x 3 : 9
    taille = np.size(matrice[:, 0])# si 3 x 3 : 3
    det = 1
    for i in range(taille):
        det *= matrice[i][i]
    return det
#-------------------------------------
def afficherMatrice(matrice):
    print('La matrice est :')
    print(matrice)
#-------------------------------------
def remplaceLigne(matrice, indicePivot, indiceLigne, colonnePivot):
    pivot = np.copy(matrice[indicePivot, :])
    ligne = np.copy(matrice[indiceLigne, :])
    
    tailleLigne = np.size(pivot)
    coefficient = ligne[colonnePivot]/pivot[colonnePivot]

    for i in range(tailleLigne):
        ligne[i] = coefficient*pivot[i] - ligne[i]
    
    matrice[indiceLigne, :] = ligne
#-------------------------------------
def triangleSuperieur(matrice):
 
    nombreLigne = matrice.shape[0] #shape[0] nombre de ligne
    n = (nombreLigne - 1) #matrice n x n
    nombreColonne = matrice.shape[1] #shape[1] nombre de colonne
   
    vecteur = np.copy(matrice[:, nombreColonne - 1])
    solution = np.zeros(nombreLigne) #vecteur
    
    solution[n] = vecteur[n] / matrice[n, n]
    
    for i in range(n-1, -1, -1): # de n-1 à 0
        somme = 0
        for j in range(n, i, -1):
            somme += matrice[i, j] * solution[j]
        solution[i] = (vecteur[i] - somme) / matrice[i, i]
    
    return solution

#-------------------------------------
        
print('Veuillez saisir une matrice carrée (nombre de ligne = nombre de colonne)')

while(True): # while(1):
    n1 = int(input('Veuillez saisir le nombre de ligne de la matrice :\n'))
    n2 = int(input('Veuillez saisir le nombre de colonne de la matrice :\n'))
    if n1 != n2:
        print('Veuillez saisir la matrice avec (nombre de ligne = nombre de colonne)')
    if n1 == n2:
        break


matrice = np.zeros([n1, n2+1])


print('Veuillez renseigner la matrice : [', n1,', ', n2,'] :')
for i in range(n1):
    for j in range(n2):
        matrice[i][j] = float(input('matrice['+str(i)+']['+ str(j)+'] = '))


print('Veuillez saisir le vecteur :')

vecteur = np.zeros(n1)

for i in range(np.size(vecteur)):
    vecteur[i] = float(input('['+str(i)+'] = '))
    
matrice[:, n2] = vecteur

afficherMatrice(matrice)

# remplaceLigne(matrice, 0, 1, 0) # remplaceLigne(matrice, indicePivot, indiceLigne, colonnePivot)
for i in range(n1 - 1): # boucle i (lignes pivots) de 0 à n-1
    for j in range(i+1, n1): # boucle j (lignes) de (lignes pivots)+1 à n
        remplaceLigne(matrice, i, j, i)

afficherMatrice(matrice)

det = determinantMatriceTriangulaire(matrice)


if(det == 0):
    print('Le determinant de la matrice vaut : ', det, ' . Il n\'y a pas de solution unique')
else:
    print('Le determinant de la matrice vaut : ', det)
    print('La solution : ', triangleSuperieur(matrice))
  




    

