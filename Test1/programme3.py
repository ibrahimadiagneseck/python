import numpy as np

vecteur = np.array([1, 2, 3])
matrice = np.array([[1, 2, 3], [4, 5, 6]])

# np.transpose(matrice)
# matrice.transpose()
# matrice.T
print('------------------')
print(vecteur, end="\n\n")
print(matrice, end="\n\n")
print('------------------')
print(matrice.T, end="\n\n")
print('------------------')
print(np.array([[1, 2, 3]]).T, end="\n\n")
print('------------------')
print(vecteur.T, end="\n\n")
print(np.atleast_2d(vecteur), end="\n\n")
print(np.atleast_2d(vecteur).T, end="\n\n")
print('------------------')
print(vecteur, end="\n\n")
print(vecteur[1], end="\n\n")
print(matrice[0,0], end="\n\n")
print(matrice[0,:], end="\n\n")
print(matrice[:,0], end="\n\n")

