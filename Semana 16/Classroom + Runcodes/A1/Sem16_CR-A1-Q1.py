def preencherMatriz(n):
    matriz = []
    for lin in range(n):
        linha = []
        for col in range(n):
            linha.append(int(input(f'Digite os valores da {lin + 1}ª linha e {col + 1}ª coluna: ')))
        matriz.append(linha)
    return matriz

def maiorElemento(matriz):
    l = 0
    c = 0
    maior = matriz[0][0]
    for i_linha in range(len(matriz)):
        for i_coluna in range(len(matriz[i_linha])):
            if matriz[i_linha][i_coluna] > maior:
                maior = matriz[i_linha][i_coluna]
                l = i_linha
                c = i_coluna
    return l, c

def menorElemento(matriz):
    menor = matriz[0][0]
    l = 0
    c = 0
    for i_linha in range(len(matriz)):
        for i_coluna in range(len(matriz[i_linha])):
            if matriz[i_linha][i_coluna] < menor:
                menor = matriz[i_linha][i_coluna]
                l = i_linha
                c = i_coluna
    return l, c

def main():
    n = int(input('Digite o número de linhas e colunas da matriz quadrada: '))
    matrizQuadrada = preencherMatriz(n)
    maior = maiorElemento(matrizQuadrada)
    menor = menorElemento(matrizQuadrada)
    print(f'O maior elemento da matriz está na posição {maior}')
    print(f'O menor elemento da matriz está na posição {menor}')
    
if __name__ == '__main__':
    main()