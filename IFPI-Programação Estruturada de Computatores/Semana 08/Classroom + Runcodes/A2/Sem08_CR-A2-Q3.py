# Define a função divisao recebendo um parâmetro
def divisao(n1):
# Se n1 for maior que 0, inicia outra estrutura condicional
    if n1 > 0:
    # Se os restos das divisões das variáveis n1 por 3 e 5 for igual a 0, retorna a formatação de string 'FIZZBUZZ' 
        if n1 % 3 == 0 and n1 % 5 == 0:
            return f'FIZZBUZZ'
    # Se o comentário acima for falso e o resto da divisão da variável n1 por 3 for igual a 0, retorna a formatação de string 'FIZZ'
        elif n1 % 3 == 0:
            return f'FIZZ'
    # Se o comentário acima for falso e o resto da divisão da variável n1 por 5 for igual a 0, retorna a formatação de string 'BUZZ'
        elif n1 % 5 == 0:
            return f'BUZZ'
    # Se os comentário acimas forem falsos, retorna a variável n1
        else:
            return n1
    # Se n1 for igual ou menor que 0, retorna n1
    else:
        return n1
        
def main():
    
    #Entrada
    n1 = int(input('Digite um número inteiro: '))
    
    #Processamento
    resultado = divisao(n1)

    #Saída
    print(f'{resultado}')
         
if __name__ == '__main__':
    main()