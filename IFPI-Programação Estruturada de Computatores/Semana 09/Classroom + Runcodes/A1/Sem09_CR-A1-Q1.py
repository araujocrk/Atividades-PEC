# Define a função igual_ou_diferente recebendo 3 parâmetros
def igual_ou_diferente(a, b, c):
    # Se a variável 'a' for igual a variável 'b' e a 'a' ser igual a variável 'c'
    if a == b and a == c:
    # Retorna a str 'todos os valores são iguais'
        return f'todos os valores são iguais'
    # Se o if acima for falso e os valores de duas variáveis forem iguais e uma diferente 
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    # Retorna a str 'existem dois valores iguais e um diferente'
        return f'existem dois valores iguais e um diferente'
    # Se o elif acima for falso e os valores de todas as variáveis forem diferentes
    elif a != b and b != c and a != c:
    # Retorna a str 'todos os valores são diferentes'
        return f'todos os valores são diferentes'

def main():
    
    #Entrada
    n1 = int(input('Digite o 1º número inteiro: '))
    n2 = int(input('Digite o 2º número inteiro: '))
    n3 = int(input('Digite o 3º número inteiro: '))
    
    #Processamento
    resultado = igual_ou_diferente(n1, n2, n3)
    
    #Saída
    print(f'Analisando seus números, {resultado}')
    
    
    
if __name__ == '__main__':
    main()