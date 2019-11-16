def readFile(): # Funcao que le matriz do arquivo
    arq = open('LU/SISTEMA.txt','r')
    matriz = []
    texto = arq.readlines()
    rows, columns = 0, 0
    for i in range(len(texto)):
        matriz.append(list(map(int,texto[i].split())))
        columns = len(texto[i].split())
        rows += 1
    arq.close()
    return matriz, rows, columns # Retorna a matriz, numero de linhas e colunas