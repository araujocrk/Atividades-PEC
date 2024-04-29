def diferenca(a, b, c):
    d1 = abs(a - b)
    d2 = abs(a - c)
    return d1, d2
def menor(a, b, c):
    d1, d2 = diferenca(a, b, c)
    if d1 < d2:
        return d1
    else:
        return d2 
def main():
    
    #Entrada
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    
    #Processamento
    resultado = menor(n1, n2, n3)
    
    #Saída
    print(f'{resultado}')
    
if __name__ == '__main__':
    main()