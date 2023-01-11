import numpy as np
import sys

n = int(input('Entrer n: '))

a = np.zeros((n,n+1))

x = np.zeros(n)

print('renseigner la matrice:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Division par zero!')
        
    for j in range(i+1, n):
        sub = a[j][i]/a[i][i]
        
        for m in range(n+1):
            a[j][m] = a[j][m] - sub * a[i][m]

x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

print('La solution est: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')


