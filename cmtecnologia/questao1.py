tamanho = 15  # quantidade desejada de linhas/colunas na matrix

"""
    A próxima linha é utilizada para construir uma matrix de forma automática
    um 'for' constroi as linhas, esse por sua vez retorna uma lista 
    também construida utilizando 'for' para fazer as colunas
"""
matriz = [[i + 1 for i in range(tamanho)] for i in range(tamanho)]


# Função que percorre as linhas e colunas de uma Matrix e a imprime de forma legivel
def printMatriz(matriz):
    for i in range(len(matriz)):
        print(" | ", end="")
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("| ")


def inverte(matriz):
    """
    a variável 'temp' é utilizada para marcar a próxima coluna a ser trocada
    no inicio é -1, já que ainda não trocou nenhum valor
    no decorrer do programa ela vai diminuindo
    assim, na linha 1, temos 'temp' = -1, na 2 'temp' = -2
    e assim por diante até temp ter o valor oposto de tamanho, |temp| == tamanho
    exemplo:
        inicio: [1,2,3,4,5] --> temp = -1
        temp -= 1 --> temp = -2
        fim: [5, 2, 3, 4, 1]
    """

    temp = -1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j], matriz[i][temp] = matriz[i][temp], matriz[i][j]
                temp -= 1
    return matriz


print("--   Começo  --")
printMatriz(matriz)

print("--    Fim    --")
printMatriz(inverte(matriz))
