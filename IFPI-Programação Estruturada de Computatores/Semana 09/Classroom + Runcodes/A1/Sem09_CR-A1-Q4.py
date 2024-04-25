# Define a função diferenca recebendo 3 parâmetros
def diferenca(a, b, c):
    # A variável d1 recebe o número absoluto da subtração das variáveis a - b
    d1 = abs(a - b)
    # A variável d2 recebe o número absoluto da subtração das variáveis a - c
    d2 = abs(a - c)
    # Retorna as variáveis d1 e d2
    return d1, d2

# Define a função menor recebendo 3 parâmetros
def menor(a, b, c):
    # As variáveis d1 e d2 recebem o retorno da função diferenca mandando 'a', 'b' e 'c' como parâmetros
    d1, d2 = diferenca(a, b, c)
    # Se f1 for menor que d2
    if d1 < d2:
        # Retorna a variável d1
        return d1
    # Se if for falso
    else:
        # Retorna a variável d2
        return d2 
    
def main():
    
    #Entrada
    n1 = int(input('Digite o 1º número inteiro: '))
    n2 = int(input('Digite o 2º número inteiro: '))
    n3 = int(input('Digite o 3º número inteiro: '))
    
    #Processamento
    resultado = menor(n1, n2, n3)
    
    #Saída
    print(f'A menor diferença é {resultado}')
    
if __name__ == '__main__':
    main()