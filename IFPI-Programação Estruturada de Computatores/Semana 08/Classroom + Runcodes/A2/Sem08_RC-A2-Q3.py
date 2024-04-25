def divisao(n1):
    if n1 > 0:
        if n1 % 3 == 0 and n1 % 5 == 0:
            return f'FIZZBUZZ'
        elif n1 % 3 == 0:
            return f'FIZZ'
        elif n1 % 5 == 0:
            return f'BUZZ'
        else:
            return n1
    else:
        return n1
        
def main():
    
    #Entrada
    n1 = int(input().strip())
    
    #Processamento
    resultado = divisao(n1)

    #Saída
    print(f'{resultado}')
         
if __name__ == '__main__':
    main()