import numpy as np
import math 

# pivot de Gauss
# boucle i (lignes pivots) de 1 à n-1
# boucle k (lignes) de i+1 à n
# l1 <- (L2 / L1) L1 - L2

def determinant(matrice):
    taille = np.size(matrice)
    det = 1
    for i in range(taille-1):
        det *= matrice[i][i]
    return det

def afficherMatrice(matrice):
    print('La matrice est :')
    print(matrice)

def remplaceLigne(matrice, indicePivot, indiceLigne, colonnePivot):
    pivot = np.copy(matrice[indicePivot, :])
    ligne = np.copy(matrice[indiceLigne, :])
    
    tailleLigne = np.size(pivot)
    coefficient = ligne[colonnePivot]/pivot[colonnePivot]

    for i in range(tailleLigne):
        ligne[i] = coefficient*pivot[i] - ligne[i]
    
    matrice[indiceLigne, :] = ligne

        
print('Veillez saisir une matrice carrée (nombre de ligne = nombre de colonne)')

# n1 = int(input('Veillez saisir le nombre de ligne de la matrice :\n'))
# n2 = int(input('Veillez saisir le nombre de colonne de la matrice :\n'))

while(True): # while(1):
    n1 = int(input('Veillez saisir le nombre de ligne de la matrice :\n'))
    n2 = int(input('Veillez saisir le nombre de colonne de la matrice :\n'))
    if n1 != n2:
        print('Veillez saisir la matrice avec (nombre de ligne = nombre de colonne)')
    if n1 == n2:
        break


print('Veillez saisir le vecteur :\n')
vecteur = np.zeros(n1)
for i in range(np.size(vecteur)):
    vecteur[i] = float(input())


matrice = np.zeros([n1, n2+1])


print('Veillez renseigner la matrice : [', n1,', ',n2,'] :\n')
for i in range(n1):
    for j in range(n2):
        matrice[i][j] = float(input('matrice['+str(i)+']['+ str(j)+'] = '))

matrice[:, n2] = vecteur

afficherMatrice(matrice)

# remplaceLigne(matrice, 0, 1, 0) # remplaceLigne(matrice, indicePivot, indiceLigne, colonnePivot)
for i in range(n1 - 1): # boucle i (lignes pivots) de 0 à n-1
    for j in range(i+1, n1): # boucle j (colonnes pivots) de 0 à n
        remplaceLigne(matrice, i, j, i)

afficherMatrice(matrice)

