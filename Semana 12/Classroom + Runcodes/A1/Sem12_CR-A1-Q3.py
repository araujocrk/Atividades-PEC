def main():
    # Inicializa o contador de anos que é necessário para o país ultrapassar 
    ano = 0
    # As constantes guardam as taxas de natalidade dos países com maior e menor população 
    TN_MAIOR = 2 / 100
    TN_MENOR = 3 / 100
    
    # Entrada de dados
    pA = aux1 = int(input('Digite quantas pessoas tem no país A: '))
    pB = aux2 = int(input('Digite quantas pessoas tem no país B: '))
    
    # Processamento
    # Se país A for maior que país B...
    if pA > pB:
        # Enquanto país A for maior que país B, será somado a cada população a taxa de natalidade por ano
        while pA > pB:
            pA += pA * TN_MAIOR
            pB += pB * TN_MENOR
            ano += 1
            aux1 = 'A'
            aux2 = 'B'
    else:
        while pB > pA:
            pA += pA * TN_MENOR
            pB += pB * TN_MAIOR
            ano += 1
            aux1 = 'B'
            aux2 = 'A'
    
    # Saída de dados
    print(f'A população do país {aux2} irá ultrapassar a população do país {aux1} em {ano} anos')

if __name__ == "__main__":
    main()