import numpy as np

vecteur1 = np.zeros(4) #vecteur à 0
matrice1 = np.zeros([2,4])

print('------------------')
print(vecteur1, end="\n\n")
print(matrice1, end="\n\n")
print('------------------')

matrice2 = np.ones([2,4]) #matrice à 1

print('------------------')
print(matrice2, end="\n\n")
print(3*matrice2, end="\n\n") #matrice à 3
print('------------------')

matrice3 = np.eye(3) # 3 ligne 3 colonne : matrice identite
matrice4 = np.eye(3, 4) 


print('------------------')
print(matrice3, end="\n\n")
print(matrice4, end="\n\n")
print('------------------')

print('------------------')
print(np.linspace(0, 1, 10), end="\n\n") # vecteur
print(np.arange(0, 10, 2), end="\n\n") # vecteur [debut fin[ pas
print('------------------')

vecteur2 = np.array([1, 2, 3, 4])

print('------------------')
print(np.diag(vecteur2), end="\n\n") # matrice
print(np.diag(vecteur2, 2), end="\n\n") # matrice
print(np.diag(vecteur2, -2), end="\n\n") # matrice
print('------------------')

print('------------------')
print(np.diag(2*np.ones(5), 0) + np.diag(-1*np.ones(4), -1) + np.diag(-1*np.ones(4), 1), end="\n\n") # matrice
print('------------------')

