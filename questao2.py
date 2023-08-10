matrizA = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]

matrizB = [[]]


def contaSubM(matriz, submatriz):
    # Evitar bug
    if submatriz == [[]] or submatriz == []:
        return 0

    qtdLinM = len(matriz)  # Quantidade de Linhas da Matriz
    qtdColM = len(matriz[0])  # Quantidade de Colunas da Matriz
    qtdLinSB = len(submatriz)  # Quantidade de Linhas da Sub-Matriz
    qtdColSB = len(submatriz[0])  # QUantidade de Colunas da Sub-Matriz
    qtdEnc = 0  # Quantidade de Sub-Matrizes

    # Não é necessário ir até o final das linhas e colunas
    # só até o ponto que poderia ter a formação da submatriz
    for i in range(qtdLinM - qtdLinSB + 1):
        for j in range(qtdColM - qtdColSB):
            temp = matriz[i : i + qtdLinSB]  # Linhas a comparar
            temp = [
                [line[j + col] for col in range(qtdColSB)] for line in temp
            ]  # Seleciona as colunas a serem comparadas
            if temp == submatriz:
                qtdEnc += 1

    return qtdEnc


print(contaSubM(matrizA, matrizB))
