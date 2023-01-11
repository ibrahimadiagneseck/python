import numpy as np
import math 

# algorithme de la dichotomie

def dichotomie(f, a, b):
    xg = a
    xd = b
    for i in np.arange(100):
        xm = (xg + xd) / 2
        if f(xg) * f(xm) < 0:
            xd = xm
        else:
            xg = xm
    sol = (xg + xd)/2
    return sol

mafonction = lambda x: x - math.exp(-x)
resultat = dichotomie(mafonction, -2, 2)
print(resultat)
print(mafonction(resultat))




