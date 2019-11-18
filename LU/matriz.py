# Inicializa um Matriz Identidade de ordem N
def matrizIdentidade(N):
    I = []
    for i in range(N):
        I.append([0] * N)
        I[i][i] = 1
    return I


# Multiplica duas matrizes
def multiplicaMatrizes(A, B):

    # Dimensões das matrizes
    nLin_A = len(A)
    nCol_A = len(A[0])

    nLin_A = len(B)
    nCol_B = len(B[0])


    # Impossível fazer a multiplicação
    if nCol_A != nLin_A:
        return None

    # Inicializa Matriz resultante
    C = []
    for i in range(nLin_A):
        C.append([0] * nCol_B)

    # Multiplica as linhas de A com as colunas de B
    for i in range(nLin_A):
        for j in range(nCol_B):
            acc = 0

            for k in range(nLin_A):
                acc += A[i][k] * B[k][j]

            C[i][j] = acc

    return C

# 
def imprimeMatriz(A):
    N = len(A)

    for i in range(N):
        print("  [", end=" ")
        for j in range(N):
            print("%10.5f" % (A[i][j]), end=" ")
        print(" ]")
    print()
