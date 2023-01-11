import numpy as np
A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
B = np.array([[-1, 0, 2],[5, 0, -4], [8, -7, 0]])

print('------------------1')
print(A, end="\n\n")
print(B, end="\n\n")
print('--------------------2')
print(A+B, end="\n\n")
print('--------------------3')
print(A*B, end="\n\n") # pas le produit matriciel
print(np.matmul(A, B), end="\n\n") # le produit matriciel
print('--------------------')
print(A**2, end="\n\n") # pas le carre de la matrice
print(np.matmul(A, A), end="\n\n") # le carre de la matrice
print(np.linalg.matrix_power(A, 2), end="\n\n") # le carre de la matrice (puissance 2...)
print('--------------------4')
print(np.linalg.inv(A), end="\n\n") # l'inverce
print('--------------------5')
print(A.shape, end="\n\n") # nombre de ligne et colonne
print(A.shape[0], end="\n\n") # nombre de ligne 
print(A.shape[1], end="\n\n") # nombre de colonne
print('--------------------6')
print(np.arange(0, 2, 0.2), end="\n\n")
print(np.arange(0, 2, 0.2).shape[0], end="\n\n") # nombre d'element : taille
print('--------------------7')
C = np.random.rand(4, 4)
print(C, end="\n\n") # matrice aleatoire
print(C[0:2, 0:2], end="\n\n") # extraire une matrice 

D = np.linspace(0, 1, 11) 
print(D, end="\n\n")
print(D[1:5], end="\n\n") # extraire une vecteur 



print('------------------')
