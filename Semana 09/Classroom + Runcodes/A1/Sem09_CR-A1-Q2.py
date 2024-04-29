# Define a função adicao recebendo dois parâmetros
def adicao(a, b):
    # Retorna a soma da variável a + b
    return a + b
# Define a função subtracao recebendo dois parâmetros
def subtracao(a, b):
    # Retorna a subtração da variável a - b
    return a - b
# Define a função multiplicacao recebendo dois parâmetros
def multiplicacao(a, b):
    # Retorna a multiplicação da variável a * b
    return a * b
# Define a função divisao recebendo dois parâmetros
def divisao(a, b):
    # Retorna a divisão da variável a / b
    return a / b

def main():
    
    #Entrada
    n1 = float(input('Digite o 1º número: '))
    n2 = float(input('Digite o 2º número: '))
    print('Qual das operações a seguir você deseja:')
    op = int(input('1 - Adição, 2 - Subtração, 3 - Multiplicação e 4 - Divisão\n'))
    
    #Processamento
    # Se a variável 'op' for igual a 1
    if op == 1:
        # A variável 'resultado' recebe o valor retornado da função adicao enviando 2 parâmetros (n1, n2)
        resultado = adicao(n1, n2)
    # Se if for falso e a variável 'op' for igual a 2
    elif op == 2:
        # A variável 'resultado' recebe o valor retornado da função subtracao enviando 2 parâmetros (n1, n2)
        resultado = subtracao(n1, n2)
    # Se elif acima for falso e a variável 'op' for igual a 3
    elif op == 3:
        # A variável 'resultado' recebe o valor retornado da função multiplicacao enviando 2 parâmetros (n1, n2)
        resultado = multiplicacao(n1, n2)
    # Se elif acima for falso e a variável 'op' for igual a 4
    elif op == 4:
        # A variável 'resultado' recebe o valor retornado da função divisao enviando 2 parâmetros (n1, n2)
        resultado = divisao(n1, n2)
    
    #Saída
    print(f'O resultado da operação é {resultado:.2f}')
    
    
    
if __name__ == '__main__':
    main()