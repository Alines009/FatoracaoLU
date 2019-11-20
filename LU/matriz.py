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

#Calcula o determinante da matriz
def calculaDeterminante(U,column):
    det = 1.0
    for i in range(column):
        det = det * U[i][i]
    return det

# Imprime uma matriz
def imprimeMatriz(A):
    N = len(A)

    for i in range(N):
        print("  [", end=" ")
        for j in range(N):
            print("%10.5f" % (A[i][j]), end=" ")
        print(" ]")
    print()

# Imprime um vetor
def imprimeVetor(A):
    print(A)
    print()

# Calcula o vetor solução por retrossubstituição
# em uma matriz triangular superior
def retrosubstituicaoSuperior(A, B):
    N = len(A)

    # Vetor solução
    S = []
    for i in range(N):
        S.append([0])

    # Resolve para última incógnita
    S[N-1][0] = B[N-1][0] / A[N-1][N-1]

    # Para cada linha acima
    for i in range(N-2, -1, -1):

        acc = 0
        for j in range(N-1, i, -1):

            acc += A[i][j] * S[j][0]

        # Atualiza vetor solução
        S[i][0] = (B[i][0] - acc) / A[i][i]

    return S


# Cálcula o vetor solução por retrosubstituição
# em uma matriz triangular inferior
def retrosubstituicaoInferior(A, B):
    N = len(A)

    # Vetor solução
    S = []
    for i in range(N):
        S.append([0])

    # Resolve para primeira incógnita
    S[0][0] = B[0][0] / A[0][0]

    # Para cada linha abaixo
    for i in range(0, N):

        acc = 0
        for j in range(0, i):

            acc += A[i][j] * S[j][0]

        # Atualiza vetor solução
        S[i][0] = (B[i][0] - acc) / A[i][i]

    return S


# Calcula a matriz inversa de A, decomposta nas matrizes L e U
def matrizInversa(L, U, B):

    # Resolve os sistemas para cada coluna de B
    for col in range(len(B)):

        # Cria o vetor dos termos independentes
        colunaB = []
        for lin in range(len(B[0])):
            colunaB.append([B[lin][col]])

        # Resolva o sistema LY = B
        Y = retrosubstituicaoInferior(L, colunaB)

        # Resolva o sistema UX = Y
        X = retrosubstituicaoSuperior(U, Y)
        # X é a coluna da 
        
        for i in range(len(B)):
            B[i][col] = X[i][0]

    return B
