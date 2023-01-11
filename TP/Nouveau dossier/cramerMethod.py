def laplace(A, val=1):

    n = len(A)

    if n == 1:
        return val * A[0][0]
    else:
        sign = -1
        det = 0
        for i in range(n):
            mtx = []
            for j in range(1, n):
                buff = []
                for k in range(n):
                    if k != i:
                        buff.append(A[j][k])
                mtx.append(buff)
            sign *= -1
            det += val * laplace(mtx, sign * A[0][i])
        return det

def cramer(A, results, n):
    main_det = laplace(A)
    print(f'\nLe Déterminant de la matrice principale est : {main_det}')

    if main_det != 0:
        resolution = []
        for r in range(n):
            substitution = []
            for i in range(n):
                substitution.append([])
                for j in range(n):
                    if j == r:
                        substitution[i].append(results[i])
                    else:
                        substitution[i].append(A[i][j])

            print(f'\nMatrice de substitution à la colonne {r + 1}:')
            for line in substitution:
                for val in line:
                    print(f'{val:^8}', end=' ')
                print()

            sub_det = laplace(substitution)//main_det
            print(f'Determinant : {sub_det}')

            resolution.append(sub_det / main_det)

        return resolution

    else:
        return 0

def main():
    n = int(input('Entrer n: '))

    print(f'Entrer la matrice {n}x{n} avec des espaces (pour les colonnes) et entrer (pour les lignes):')
    A = [list(map(float, input().split())) for i in range(n)]

    results = list(map(float, input('Entrer la matrice à une colonne avec des espaces (pour la colonne): ').split()))

    resolution = cramer(A, results, n)
   
main()
