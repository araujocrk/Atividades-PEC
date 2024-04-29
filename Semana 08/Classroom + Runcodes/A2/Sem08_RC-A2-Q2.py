def soma(n1):
    n = n1
    u = n1 % 10
    n1 = n1 // 10
    d = n1 % 10
    n1 = n1 // 10
    c = n1 % 10
    n1 = n1 // 10
    m = n1 % 10
    n1 = n1 // 10
    dm = n1 % 10
    n1 = n1 // 10
    cm = n1 % 10
    if 0 < n < 100000:
        return u + d + c + m + dm + cm
    else:
        return -1 

def main():
    
    #Entrada
    n1 = int(input().strip())
    
    #Processamento
    resultado = soma(n1)

    #Saída
    print(f'{resultado}')

         
    
    
    
if __name__ == '__main__':
    main()