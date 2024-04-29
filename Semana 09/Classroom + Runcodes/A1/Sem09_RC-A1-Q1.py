def igual_ou_diferente(a, b, c):
    if a == b and a == c:
        return f'Todos os valores são iguais'
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return f'Existem dois valores iguais e um diferente'
    elif a != b and b != c:
        return f'Todos os valores são diferentes'

def main():
    
    #Entrada
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    
    #Processamento
    resultado = igual_ou_diferente(n1, n2, n3)
    
    #Saída
    print(f'{resultado}')
    
    
    
if __name__ == '__main__':
    main()