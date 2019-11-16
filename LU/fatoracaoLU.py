from files import readFile

def changeRows(i,j): #Funcao que troca as linhas da matriz
    for k in range(len(matriz)):
        print(matriz[k])
    aux = matriz[i]
    matriz[i] = matriz[j]
    matriz[j] = aux
    print("--------------")
    for k in range(len(matriz)):
        print(matriz[k])
    print("~~~~~~~~~~")
    return matriz

def pivoting(matriz, i):
    if(i!=len(matriz)-1):
        num = matriz[i][i]
        den = matriz[i+1][i]
        print("O numerador e denominador sao: ",num,den)


def gauss(matriz):
    for i in range(len(matriz)):
        pivo = matriz[i][i]  # O primeiro pivo selecionado é o elemento da diagonal
        for j in range(i + 1,columns):
            print(matriz[j][i])
            if (matriz[j][i] > pivo):  # Se houver elementos na coluna que é maior que o pivo, este será o novo pivo
                pivo = matriz[j][i]
                print(pivo)
                matriz = changeRows(i, j)

        pivoting(matriz,i)

matriz,rows, columns = readFile()
gauss(matriz)

