def resultado_div(a, n):
    if a == 0:
        return (9 * n) + 7
    elif a == 1:
        if n % 2 == 0:
            return 'par'
        else:
            return 'ímpar'
    elif a == 2:
        return (5 * (n ** 2)) - (3 * n) + 42
    elif a == 3:
        return n // 10
    elif a == 4:
        return n ** 2
        
def main():
    
    #Entrada
    n1 = int(input().strip())
    
    #Processamento
    resto = n1 % 5
    resultado = resultado_div(resto, n1)
    
    #Saída
    print(f'{resultado}')
    
if __name__ == '__main__':
    main()