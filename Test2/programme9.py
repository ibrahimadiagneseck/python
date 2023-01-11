import numpy as np

vecteur = np.array([1, 2, 3])

print(np.atleast_2d(vecteur), end="\n\n")
print(np.atleast_2d(vecteur).T, end="\n\n")

print(vecteur.T, end="\n\n")