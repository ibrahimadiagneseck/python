print("Entrer n:")
L=int(input("n : "))

C = L

matrice = [[0 for i in range(C)] for j in range(L)]

for i in range(L):
    for j in range(C):
        matrice[i][j] = int(input("Saisir matrice[{0}][{1}] : ".format(i, j)))
    
def matrice_cut(m,i):
    mbis=[list(j) for j in m]
    coeff=mbis[i][0]
    mbis.remove(mbis[i])
    for k in mbis:
        k.remove(k[0])
    return coeff,mbis

def det(m):
    det=0
    if len(m)==1:
        det=m[0]
    elif len(m)==2:
        det=m[0][0]*m[1][1]-m[1][0]*m[0][1]
    else:
        for j in range(0,len(m)):
            mem=matrice_cut(m,j)
            det=det+(((-1)**j)*mem[0]*det(mem[1]))
    return det

print("Le det est: ",det(matrice)) 

estTriangInf = True

for j in range(C):
    for i in range(j):
        if(matrice[i][j] != 0):
            estTriangInf = False
        break

if(estTriangInf == True):
    print("\nLa matrice est triangulaire inférieure.")
    somme = 0
    for i in range(L):
        for j in range(i-1, C):
            somme += matrice[i][j]

    print("Et La somme est ", somme)
else:
    print("\nLa matrice n'est pas triangulaire supérieure.") 

