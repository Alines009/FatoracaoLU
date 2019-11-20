def readFile(): # Funcao que le matriz do arquivo
    arq = open('LU/SISTEMA.txt','r')
    matriz = []
    texto = arq.readlines()
    rows, columns = 0, 0
    for i in range(len(texto)):
        matriz.append(list(map(float,texto[i].split())))
        columns = len(texto[i].split())
        rows += 1
    arq.close()
    return matriz, rows, columns # Retorna a matriz, numero de linhas e colunas


# Escreve a matriz resultante no arquivo
def writeFile(matriz):
    arq = open('RESUL.txt', 'w')

    N = len(matriz)

    for i in range(N):
        x = ""
        for j in range(N):
            x += "%10.5f" % (matriz[i][j])
        
        arq.write(x + "\n")
    
    arq.close()
