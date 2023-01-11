import numpy as np
import math

##R11 = sqrt(a11)
##
##for j = 2 ... n
##
##    for i = 1 ... j-1
##        sommeK = 0
##        for k = 1 ... i-1
##            sommeK += Rki.Rkj
##        Rij = 1 / Rii ( aij - sommeK )
##        
##    sommeK = 0
##    for k = 1 ... j-1
##        sommeK += (Rkj)**2
##    Rjj = sqrt( ajj - sommeK )
    


## lij = sqrt( aij - Σ k=1..j-1 (lik)^2 ), i = j 
##                                                           i = j..n       j = 1..n
## lij = 1/lji  [aij - Σ k=1..j-1 (lik ljk)], i != j 

#----------------------------------------
def recupererMatriceA(matrice, taille):
    
    A = np.zeros([taille, taille])
    
    for i in range(taille):
        for j in range(taille):
            A[i, j] = matrice[i, j]
            
    return A
#----------------------------------------
def decompostionCholesky(matrice):

    n = matrice.shape[0]
    A = recupererMatriceA(matrice, n)
    R = np.zeros_like(A)

    R[0, 0] = np.sqrt(A[0, 0])
            
    for j in range(1, n):
        for i in range(j):
                sommeK = 0
                for k in range(i):
                    sommeK += R[k, i] * R[k, j]
                R[i, j] = (1 / (R[i, i])) * (A[i, j] - sommeK)
                
        sommeK = 0
        for k in range(j):
            sommeK += R[k, j] ** 2
        R[j, j] = np.sqrt(A[j, j] - sommeK)
    
    return np.atleast_2d(R).T
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
def determinantMatriceTriangulaire(matrice):
    #taille = np.size(matrice)# si 3 x 3 : 9
    taille = np.size(matrice[:, 0])# si 3 x 3 : 3
    det = 1
    for i in range(taille):
        det *= matrice[i][i]
    return det
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

A = recupererMatriceA(matrice, n1)
At = np.atleast_2d(A).T

if(np.array_equal(A, At)): # A = RRt si A == At
    print('A = R.Rt')
    R = decompostionCholesky(A)
    Rt = np.atleast_2d(R).T
    print('La matrice symétrique A (définie positive) est :\n', A)
    print('La matrice décomposée est :\n', R)
    print('La transposée de la matrice décomposée est :\n', Rt)
    print('Le produit R.Rt est :\n', np.matmul(Rt, Rt))
    
    if(determinantMatriceTriangulaire(R) > 0):
        print('La décomposition de la matrice est unique')
        print('R.y = b && Rt.x = y')
        
        print('R.y = b')
        R1 = np.append(R, np.atleast_2d(vecteur).T, axis = 1)
        print(R1)
        print('La solution y = ', triangleInferieur(R1))

        print('Rt.x = y')
        R2 = np.append(Rt, np.atleast_2d(triangleInferieur(R1)).T, axis = 1)
        print(R2)
        print('La solution x = ', triangleSuperieur(R2))
    else:
        print('La décomposition de la matrice n\'est pas unique')
        
else:
    print('La matrice n\'est pas symétrique')


    
    
