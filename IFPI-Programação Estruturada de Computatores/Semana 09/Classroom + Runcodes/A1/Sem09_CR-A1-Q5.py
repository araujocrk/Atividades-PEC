# Define a função resultado_div recebendo 1 parâmetro
def resultado_div(a, n):
    # Se 'a' for igual a 0
    if a == 0:
        # Retorna 9 vezes a variável 'n' mais 7
        return (9 * n) + 7
    # Se if for falso e 'a' for igual a 1
    elif a == 1:
        # E se o resto da divisão de 'n' por 2 for igual a 0
        if n % 2 == 0:
            # Retorna a str 'par'
            return 'par'
        # Se o if acima for falso 
        else:
        # Retorna a str 'ímpar'
            return 'ímpar'
    # Se o elif acima for falso e 'a' for igual a 2
    elif a == 2:
        # Retorna a resultado de (5 * (n ** 2)) - (3 * n) + 42
        return (5 * (n ** 2)) - (3 * n) + 42
    # Se o elif acima for falso e 'a' for igual a 3
    elif a == 3:
        # Retorna a divisão inteira por 10
        return n // 10
    # Se o elif acima for falso e 'a' for igual a 4
    elif a == 4:
        # Retorna 'n' elevado a 2
        return n ** 2
        
def main():
    
    #Entrada
    n1 = int(input('Digite um número inteiro: '))
    
    #Processamento
    resto = n1 % 5
    resultado = resultado_div(resto, n1)
    
    #Saída
    print(f'{resultado}')
    
if __name__ == '__main__':
    main()