def par5_impar8(n1):
    if n1 % 2 == 0:
        return n1 + 5
    else:
        return n1 + 8

def main():
    
    #Entrada
    n1 = int(input().strip())
    
    #Processamento
    resultado = par5_impar8(n1)

    #Saída
    print(f'{resultado}')
    
    
    
if __name__ == '__main__':
    main()