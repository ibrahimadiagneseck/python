import numpy as np
import math 

## Matrice A = Lower * Upper
## 
##     |a11 ............. a1n|    |1    0 ............. 0|  |u11  ............. u1n|
##     |.                    |    |l21  1               0|  |0   u22              .|
## A = |.                    | =  |.                    0|  |0        u33         .|
##     |.                    |    |.              1     0|  |0                .   .|
##     |an1 ............. ann|    |ln1 ......... lnn-1  1|  |0 ...............0 unn|
##
## A x = b  ,  b appartient R^n
##
## A = L.U    L.U.x = b
## L.y = b && U.x = y
##
## lij = aij - Σ k=1..j-1 (lik ukj), j <= i, i = 1...n 
##
## uij = 1/lii  [aij - Σ k=1..i-1 (lik ukj)], i <= j, j = 1...n

#----------------------------------------
def recupererMatriceA(matrice, taille):
    
    A = np.zeros([taille, taille])
    
    for i in range(taille):
        for j in range(taille):
            A[i, j] = matrice[i, j]
            
    return A
#----------------------------------------
def decompostionLU(matrice):

    n = matrice.shape[0]
    A = recupererMatriceA(matrice, n)
            
    L = np.eye(n)
    U = np.copy(A)

    for i in range(n):
        tmp = U[i, i]
        for j in range(i+1, n):
            L[j, i] = U[j, i] / tmp
            U[j] = U[j] - L[j, i] * U[i]    
                
    
    return L, U
#-------------------------------------
def triangleInferieur(matrice):
 
    nombreLigne = matrice.shape[0] #shape[0] nombre de ligne
    n = (nombreLigne - 1) #matrice n x n
    nombreColonne = matrice.shape[1] #shape[1] nombre de colonne
   
    vecteur = np.copy(matrice[:, nombreColonne - 1])
    solution = np.zeros(nombreLigne) #vecteur
    
    solution[0] = vecteur[0] / matrice[0, 0]
    
    for i in range(1, n+1): # de 0 à n
        somme = 0
        for j in range(i):
            somme += matrice[i, j] * solution[j]
        solution[i] = (vecteur[i] - somme) / matrice[i, i]
    
    return solution
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


#----------------------------------------
def afficherMatrice(matrice):
    print('La matrice est :')
    print(matrice)
#----------------------------------------

        
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


L, U = decompostionLU(matrice)       
print('La matrice L est :\n', L)
print('La matrice U est :\n', U)
print('Le produit matriciel UL vaut :\n', np.matmul(L, U))

print('L.y = b && U.x = y')
print('L.y = b')
A1 = np.append(L, np.atleast_2d(vecteur).T, axis = 1)
print(A1)
print('La solution y = ', triangleInferieur(A1))
print('U.x = y')
A2 = np.append(U, np.atleast_2d(triangleInferieur(A1)).T, axis = 1)
print(A2)
print('La solution x = ', triangleSuperieur(A2))

